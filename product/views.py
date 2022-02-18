from django.shortcuts import render
from .models import Product

# Create your views here.
def list(request):
    context={
        'list': Product.objects.all(),
    }
    return render(request, 'product/list.html', context)

def create_product(request):
    context={
        'list': Product.objects.all(),
    }
    return render(request, 'product/list.html', context)