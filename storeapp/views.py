from django.shortcuts import render,redirect
from .models import *

from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from cart.cart import Cart

from django.core.mail import send_mail

from django.db.models import Q

# Create your views here.
def index(request):
    if request.GET.get('search'):
        search = request.GET.get('search')
        search = search.lower()
        prod = Product.objects.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search) |
            Q(category__name__icontains=search)
        )

        data = {
            'productData': prod,

        }
        return render(request, 'page/product_list.html', data)

    else:
        cat = Category.objects.all()
        prod = Product.objects.all()
        data = {
            'categoryData': cat,
            'productData': prod,

        }

        return render(request, 'page/index.html', data)
# def index(request):
    
#     if request.GET.get('search'):
#         search = request.GET.get('search')
        
#         product = Product.objects.filter(name__icontains=search)
#         data = {
#             'productData' : product
#         }
#         return render(request, 'page/product_list.html', data)
        
#     else:
#         category = Category.objects.all()
#         product = Product.objects.all()
    
#         data = {
#             'categoryData' : category,
#             'productData' : product
#         }
    
#         return render(request,'page/index.html',data)

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




def contact(request):
    
    if request.method == "POST" :
       email = request.POST['email']
       subject = request.POST['subject']
       message = request.POST['message']
       send_mail(subject,message,email,['aditimaskey@kcc.edu.np'])
       return HttpResponse("Thank you for your msg")
       
    else:
        return render(request,'page/contact.html')
        
        
    