from django.urls import path
from bon_appetit_app import views

app_name = 'bon-appetit'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('top-restaurants/', views.topRestaurants, name='top-restaurants'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
