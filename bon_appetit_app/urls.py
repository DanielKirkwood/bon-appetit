from django.urls import path
from bon_appetit_app import views

app_name = 'bon-appetit'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('top-restaurants/', views.topRestaurants, name='top-restaurants'),
    path('restaurant/<slug:restaurant_name_slug>/', views.viewPage, name='view-page'),
    path('view-account/', views.viewAccount, name='view-account'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('edit-account/', views.editAccount, name='edit-account')
]
