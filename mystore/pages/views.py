from django.shortcuts import render

from .models import *


def home_page(request):
    context={
        "products": Product.objects.all() 
    }
    return render(request, 'index.html',context)

def shop_page(request):
    context={
        "products": Product.objects.all() 
    }
    return render(request, 'shop.html',context)


def get_category(request,category_id):
    product = Product.objects.filter(category_id=category_id)

def about_page(request):
    return render(request, 'about.html',{})

def shop_details_page(request):
    context={
        "products": Product.objects.all() 
    }
    return render(request, 'shop_details.html',context)

def shopping_cart_page(request):
    return render(request, 'shopping_cart.html',{})

def checkout_page(request):
    return render(request, 'checkout.html',{})

def blog_details_page(request):
    return render(request, 'blog_details.html',{})

def blog_page(request):
    return render(request, 'blog.html',{})

def contacts_page(request):
    return render(request, 'contacts.html',{})