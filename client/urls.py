from django.urls import path
from . import views

app_name='client'

urlpatterns = [
    path('', views.search, name='search'),
    path('create/', views.create, name='create'),
    path('modify/<pk>', views.modify, name='modify'),
]