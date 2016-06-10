from django.shortcuts import render
from .models import City
from .forms import AddCity


# Create your views here.

def index(request):
    cities = City.objects.all().order_by('name')
    return render(request, 'main/index.html', {'cities': cities})


def add_city(request):
    form = AddCity()
    return render(request, 'main/add_city.html', {'form': form})
