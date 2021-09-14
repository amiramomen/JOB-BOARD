from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class Info(models.Model):
    Place = models.CharField(max_length=50)
    Phone = models.CharField(max_length=15)
    Email = models.EmailField(max_length=100)
    class Meta:
        verbose_name = ("Info")
        verbose_name_plural = ("InfoS")
        

