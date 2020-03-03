from django.urls import path
from bon_appetit_app import views

app_name = 'bon-appetit'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search')
]