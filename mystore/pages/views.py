from django.shortcuts import render
from cart.forms import CartAddProductForm
from .models import *


def home_page(request):
    context={
        "products": Product.objects.all()[:8],
        "cart_form": CartAddProductForm
    }
    return render(request, 'index.html',context)

def shop_page(request):
    context={
        "categories": Category.objects.all(),
        "products": Product.objects.all(),
        "cart_form": CartAddProductForm
    }
    return render(request, 'shop.html',context)


def get_category(request,*args, **kwargs):
    context={
        "categories": Category.objects.all(),
        "products" : Product.objects.filter(category__slug=kwargs['category_slug'])
    }
    return render(request, 'shop.html', context)

def product_details(requst, *args, **kwargs):
    context={
        "product": Product.objects.get(slug=kwargs['product_slug'])
    }
    return render(requst, 'product_details.html', context)

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

