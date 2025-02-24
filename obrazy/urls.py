from django.urls import path
from . import views

urlpatterns = [
    path('', views.obraz_list, name='index'),
    path('<int:id>/', views.obraz_detail, name='detail'),
    path('new/', views.obraz_create, name='new'),
    path('edit/<int:id>/', views.obraz_edit, name='edit'),
    path('delete/<int:id>/', views.obraz_delete, name='delete'),
]