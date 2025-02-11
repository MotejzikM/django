from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:index>", views.zobrazObraz),
    path("novy/", views.novyObraz),
    path("edit/<int:index>", views.editObraz),
    path("delete/<int:index>", views.deleteObraz),
    path("<str:wrong>", views.error404),
    path("<str:wrong>/", views.error404),
]
