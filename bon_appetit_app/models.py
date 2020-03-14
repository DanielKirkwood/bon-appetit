from django.db import models
from django.template.defaultfilters import slugify


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
    picture = models.ImageField(blank=True)
    rating = models.IntegerField(default=0)

    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Restaurant, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Menu(models.Model):
    restaurant_name = models.CharField(max_length=128)
    restaurant = models.OneToOneField(
        Restaurant,
        on_delete = models.CASCADE,
        primary_key=True,
    )

class FoodItem(models.Model):
    menu = models.ForeignKey(
        Menu,
        on_delete = models.CASCADE,
        related_name='food',
    )
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    restriction = models.CharField(max_length=255, default='None')

    def __str__(self):
        return self.name

