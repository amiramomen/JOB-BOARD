from django.contrib import admin
from django.template.defaultfilters import register
from .models import Profile , City
# Register your models here.

admin.site.register(Profile)
admin.site.register(City)