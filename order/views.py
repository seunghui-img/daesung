from django.shortcuts import render
from .models import Order

# Create your views here.
def sales(request):
    context={
        'list': Order.objects.filter(biz_type=7)
    }
    return render(request, 'order/sales.html', context)
def charge(request):
    context={
        'list': ''
    }
    return render(request, 'order/charge.html', context)
def rental(request):
    context={
        'list': ''
    }
    return render(request, 'order/rental.html', context)
def uncollected_amount(request):
    context={
        'list': ''
    }
    return render(request, 'order/uncollected-amount.html', context)
def stock(request):
    context={
        'list': ''
    }
    return render(request, 'order/stock.html', context)
def dashboard(request):
    context={
        'list': ''
    }
    return render(request, 'order/dashboard.html', context)