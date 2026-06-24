from django.shortcuts import render, HttpResponse, redirect
from .models import Product

def home_page(request):
    return render(request, "homepage.html")

def western_outfits(request):
    products=Product.objects.filter(
        category=1
    )
    return render(request, "western.html", {"products": products})

def traditional_outfits(request):
    products=Product.objects.filter(
        category=2
    )
    return render(request, "traditional.html", {"products": products})

def accessories(request):
    products=Product.objects.filter(
        category=3
    )
    return render(request, "accessories.html", {"products": products})

def daily_products(request):
    products=Product.objects.filter(
        category=4
    )
    return render(request, "products.html", {"products": products})

def product_details(request, id):
    product=Product.objects.get(id=id)
    return render(request, 'product-details.html', {'product': product})
# Create your views here.
