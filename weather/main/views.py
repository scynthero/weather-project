from django.shortcuts import render
from .models import City
from .forms import AddCity
from django.shortcuts import redirect


# Create your views here.

def index(request):
    cities = City.objects.all().order_by('name')
    return render(request, 'main/index.html', {'cities': cities})


def add_city(request):
    if request.method == "POST":
        form = AddCity(request.POST)
        if City.objects.filter(name=request.POST['name']).exists():
            return redirect('/')
        else:
            if form.is_valid():
                city = form.save()
                city.save()
                return redirect('/')
    else:
        form = AddCity()
    return render(request, 'main/add_city.html', {'form': form})
