from django.shortcuts import render
from .models import Client

# Create your views here.
def index(request):
    context={
        'list': Client.objects.all(),
    }
    return render(request, 'client/list.html', context)