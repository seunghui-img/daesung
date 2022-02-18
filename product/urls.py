from django.urls import path
from . import views

app_name='product'

urlpatterns = [
    path('', views.list, name='list'),
    path('create/', views.create_product, name='create'),
]