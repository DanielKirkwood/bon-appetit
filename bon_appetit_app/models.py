from django.db import models

class City(models.Model):
    name = models.CharField(max_length=128, unique=True)
    
    class Meta:
        verbose_name_plural = 'Cities'
    
    def __str__(self):
        return self.name




class Restaurant(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, unique=True)
    address = models.CharField(max_length=128, unique=True)
    menu = models.CharField(max_length=128)
    price = models.IntegerField(default=0)
    picture = models.ImageField(default=0)
    rating = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name


# Create your models here.
