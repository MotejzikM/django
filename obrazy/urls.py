from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect
from . import views

urlpatterns = [
    path('', views.home_page),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('obrazy/', include('obrazyapp.urls')),
]
