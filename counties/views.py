from django.shortcuts import render
from .models import County
def homepage(request):
    counties =County.objects.all()
    return render(request,'counties/homepage.html',{'counties':counties})

# Create your views here.
