from django.shortcuts import render,redirect
from .models import *

from django.contrib.auth.decorators import login_required
from cart.cart import Cart


# Create your views here.
def index(request):
    
    category = Category.objects.all()
    product = Product.objects.all()
    
    data = {
        'categoryData' : category,
        'productData' : product
    }
    
    return render(request,'page/index.html',data)

def category_list(request):
    cat = Category.objects.all()
    data = {
        'categoryData': cat
    }
    return render(request,'page/category_list.html', data)

def category_details(request,slug):
    cat = Category.objects.get(slug=slug)
    data = {
        'categoryData' :cat
    }
    return render(request, 'page/category_details.html',data)

def product_list(request):
    prod = Product.objects.all()
    data = {
        'productData' : prod
    }
    return render(request,'page/product_list.html',data)

def product_details(request,slug):
    prod = Product.objects.get(slug=slug)
    data = {
        'productData' :prod
    }
    return render(request, 'page/product_details.html',data)


# cart

@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    redirect_back = request.META.get('HTTP_REFERER')
    return redirect(redirect_back)
    


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'page/cart_detail.html')