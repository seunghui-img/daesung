from django.urls import path
from . import views

app_name='common'

urlpatterns = [
    path('search_address', views.call_daum_address, name='address'),
]