from django.shortcuts import render
from django.views import View



def add_to_cart(request):
 return render(request, 'pr/addtocart.html')

def checkout(request):
 return render(request, 'pr/checkout.html')

def customerregistration(request):
 return render(request, 'pr/customerregistration.html')

def home(request):
 return render(request, 'pr/home.html')

def orders(request):
 return render(request, 'pr/orders.html')

def product_detail(request):
 return render(request, 'pr/productdetail.html')



