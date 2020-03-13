"""bon_appetit_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from bon_appetit_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bon-appetit/', include('bon_appetit_app.urls')),
    # the above maps any URLs starting with bon-appetit/ to be handled by app
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
