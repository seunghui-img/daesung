from django.urls import path
from . import views

app_name='order'

urlpatterns = [
    path('sales/', views.sales, name='sales'),
    path('charge/', views.charge, name='charge'),
    path('rental/', views.rental, name='rental'),
    path('uncollected-amount/', views.uncollected_amount, name='uncollected-amount'),
    path('stock/', views.stock, name='stock'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
