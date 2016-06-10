from django.shortcuts import render
from .models import City


# Create your views here.

def index(request):
    cities = City.objects.all().order_by('name')
    return render(request, 'main/index.html', {'cities':cities})
