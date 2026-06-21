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

def buy_product(request, id):
    product=Product.objects.get(id=id)
    quantity=int(request.get('quantity'))
    size=int(request.get('size'))
    total_cost=product*quantity

    # Fetching details 
    if request.method=="POST":
        name=request.get('name')
        address=request.get('address')
        phone_no=request.get('phone_no')
        state=request.get('state')
        city=request.get('city')
        pincode=request.get('pincode')

    # Mode of payment
    mode=request.get('mode')
    if mode=="cash on delivery":
        print("payment needs to be done")
    else:
        print("payment  recieved")
    conetext={
    'product': product,
    'quantity': quantity,
    'size': size,
    'total_cost': total_cost,
    'name': name,
    'address': address,
    'phone_no': phone_no,
    'state': state
    'city'
}


    


# Create your views here.
