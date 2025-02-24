from django.urls import path
from . import views

urlpatterns = [
    path('', views.autor_list, name='index'),
    path('<int:id>/', views.autor_detail, name='detail'),
    path('new/', views.autor_create, name='new'),
    path('edit/<int:id>/', views.autor_edit, name='edit'),
    path('delete/<int:id>/', views.autor_delete, name='delete'),
]