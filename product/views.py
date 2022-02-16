from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    context={
        'list': Product.objects.all(),
    }
    return render(request, 'product/list.html', context)