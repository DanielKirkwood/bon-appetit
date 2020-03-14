from django.contrib import admin
from bon_appetit_app.models import Restaurant, City
from bon_appetit_app.models import UserProfile

class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'address', 'menu', 'price')

admin.site.register(Restaurant, PageAdmin)
admin.site.register(City)
admin.site.register(UserProfile)
# Register your models here.
