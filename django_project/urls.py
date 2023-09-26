"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from appDaiki import views

urlpatterns = [
  path('', views.sitedaiki, name='sitedaiki'),
  path('premiado', views.create_premiado),
  path('premiado/update/<id>', views.update_premiado),
  path('premiado/delete/<id>', views.delete_premiado),
  path('stat', views.create_stat), 
  path('stat/update/<id>', views.update_stat),
  path('stat/delete/<id>', views.delete_stat),
  path('car', views.create_car),
  path('car/update/<id>', views.update_car),
  path('car/delete/<id>', views.delete_car),
  path('admin/', admin.site.urls),
]

