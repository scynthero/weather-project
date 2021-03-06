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

    forecast = client.getForecastWeather(q=cityname, days=10)
    array = ['none'] * 10
    array1 = ['none'] * 10
    array2 = ['none'] * 10
    for i in range(0, 10):
        array[i] = forecast['forecast']['forecastday'][i]['date'], \
                    int(forecast['forecast']['forecastday'][i]['day']['avgtemp_c'])
    for i in range(0, 10):
        array1[i] = forecast['forecast']['forecastday'][i]['date']

    for i in range(0, 10):
        array2[i] = forecast['forecast']['forecastday'][i]['day']['avgtemp_c']
    return render(request, 'main/index.html', {'form1': form1, 'cityname': cityname, 'values': array, 'array1': array1,
                                               'array2': array2})


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
