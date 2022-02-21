from django.urls import path
from . import views

app_name='client'

urlpatterns = [
    path('', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('modify/<pk>', views.modify, name='modify'),
    path('popup/', views.popup, name='popup'),
]