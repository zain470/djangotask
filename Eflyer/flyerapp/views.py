from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    prod = Products.objects.all()
    
    context = {"prod":prod}
    
    return render(request, 'index.html')



def base(request):
    prod = Products.objects.all()
    
    context = {"prod":prod}
    return   render(request, 'base.html',context)


def buyc(request):
    return HttpResponse('hello world')

