from django.shortcuts import render
from apixu.client import ApixuClient, ApixuException
from .models import City
from .forms import AddCity
from .forms import ChngCity
from django.shortcuts import redirect
api_key = '538929ced9d24f99ad7190651161106'
client = ApixuClient(api_key)

# Create your views here.


def index(request):
    if request.method == "POST":
        getpost = request.POST.get('city')
        cityname = City.objects.filter(id=getpost).values_list('name')[0]
        form1 = ChngCity(request.POST)
    else:
        cityname = City.objects.filter(id=2)
        form1 = ChngCity()

    current = client.getCurrentWeather(q=cityname)
    weather = current['current']['temp_c']
    return render(request, 'main/index.html', {'form1': form1, 'weather': weather, 'cityname': cityname})


def add_city(request):
    if request.method == "POST":
        form2 = AddCity(request.POST)
        if City.objects.filter(name=request.POST['name']).exists():
            return redirect('/')
        else:
            if form2.is_valid():
                city = form2.save()
                city.save()
                return redirect('/')
    else:
        form2 = AddCity()
    return render(request, 'main/add_city.html', {'form2': form2})
