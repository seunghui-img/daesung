from django.urls import path
from . import views

app_name = 'acc'

urlpatterns = [
    path('', views.login_user, name='index'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]