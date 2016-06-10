# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=40)

#    class Meta:
#        verbose_name = "Miasto"
#        verbose_name_plural = "Miasta"

    def __str__(self):
        return self.name
