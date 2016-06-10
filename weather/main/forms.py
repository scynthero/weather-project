from django import forms

from .models import City


class AddCity(forms.ModelForm):
    class Meta:
        model = City
        fields = ('name', )
