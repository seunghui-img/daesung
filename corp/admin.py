from urllib.request import AbstractBasicAuthHandler
from django.contrib import admin
from .models import Corp

# Register your models here.
admin.site.register(Corp)