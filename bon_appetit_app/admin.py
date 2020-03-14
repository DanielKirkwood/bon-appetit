from django.contrib import admin
from bon_appetit_app.models import Restaurant, City

class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'address', 'menu', 'price')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Restaurant, PageAdmin)
admin.site.register(City)
# Register your models here.
