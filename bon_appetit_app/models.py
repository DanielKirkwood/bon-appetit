from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


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

class FoodItem(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete = models.CASCADE,
    )
    name = models.CharField(max_length=255)
    price = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    restriction = models.CharField(max_length=255, default='None')
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    DIETARY_REQUIRMENTS_CHOICES = [
        ('NA', 'None'),
        ('VA', 'Vegan'),
        ('VG', 'Vegatarian'),
    ]

    CITY_CHOICES = [
        ('NON', 'None'),
        ('GLA', 'Glasgow'),
        ('EDI', 'Edinburgh'),
        ('MAN', 'Manchester'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=128, default='')
    surname = models.CharField(max_length=128, default='')
    city = models.CharField(max_length=3, choices=CITY_CHOICES, default='NON')
    dietary_requirments = models.CharField(max_length=2, choices=DIETARY_REQUIRMENTS_CHOICES, default='NA')
    picture = models.ImageField(upload_to='profile_image', default='profile_image/defaultProfilePicture.jpg')

    def __str__(self):
        return self.user.username