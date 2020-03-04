from django.urls import path
from bon_appetit_app import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
]
