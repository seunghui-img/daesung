from django.urls import path
from . import views

app_name='client'

urlpatterns = [
    path('', views.index, name='list'),
    path('search/', views.search, name='search'),
]