from django import forms

from .models import City


class AddCity(forms.ModelForm):
    class Meta:
        model = City
        fields = ('name', )


class ChngCity(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all().order_by('name'))
