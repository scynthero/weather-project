from django.shortcuts import render
from apixu.client import ApixuClient, ApixuException
from .models import City
from .forms import AddCity
from .forms import ChngCity
from django.shortcuts import redirect
import json
api_key = '538929ced9d24f99ad7190651161106'
client = ApixuClient(api_key)

# Create your views here.

def index(request):
    current = client.getCurrentWeather(q='London')
    weather = current['current']['temp_c']
    if request.method == "POST":
        form1 = ChngCity(request.POST)
        return redirect('/')
    else:
        form1 = ChngCity()
    return render(request, 'main/index.html', {'form1': form1, 'weather': weather})


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
