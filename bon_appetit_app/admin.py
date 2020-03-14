from django.contrib import admin
from bon_appetit_app.models import Restaurant, City, Menu, FoodItem

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'address')
    prepopulated_fields = {'slug': ('name',)}

class MenuAdmin(admin.ModelAdmin):
    list_display = ('restaurant_name', 'restaurant')

class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'restriction')

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(City)
admin.site.register(Menu, MenuAdmin)
admin.site.register(FoodItem, FoodItemAdmin)
# Register your models here.
