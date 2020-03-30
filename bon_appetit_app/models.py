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
    NONE = 'NA'
    VEGAN = 'VA'
    VEGATARIAN = 'VG'
    DIETARY_REQUIRMENTS_CHOICES = [
        (NONE, 'None'),
        (VEGAN, 'Vegan'),
        (VEGATARIAN, 'Vegatarian')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=128, default='')
    surname = models.CharField(max_length=128, default='')
    dietary_requirments = models.CharField(max_length=2, choices=DIETARY_REQUIRMENTS_CHOICES, default=NONE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_image', default='profile_image/defaultProfilePicture.jpg')

    def __str__(self):
        return self.user.username