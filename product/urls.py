from django.urls import path
from . import views

app_name='product'

urlpatterns = [
    path('', views.search, name='search'),
    path('create/', views.create_product, name='create'),
]