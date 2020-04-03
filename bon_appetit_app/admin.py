from django.contrib import admin
from bon_appetit_app.models import Restaurant, City, FoodItem, UserProfile

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'address')
    prepopulated_fields = {'slug': ('name',)}

class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'name', 'price', 'restriction', 'rating')

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(City)
admin.site.register(FoodItem, FoodItemAdmin)
admin.site.register(UserProfile)
