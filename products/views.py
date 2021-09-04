from products.models import Products
from django.shortcuts import render
from django.http import HttpResponse
from .models import Products



def index(request):
    # return HttpResponse('Hello people') 
    return render(request, 'index.html')


def product(request):
    products = Products.objects.all()
    # return HttpResponse('Hello people') 
    return render(request, 'product.html',{'products':products})



def newPage(request):
    return HttpResponse('new prodcts')