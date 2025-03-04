from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):
    if request.method=='POST':
        name=request.POST['uname']
        email=request.POST['email']
        psw=request.POST['password']
        cnf_psw=request.POST['cnf_password']
        if cnf_psw==psw:
            data=User.objects.create_user(username=name,email=email,password=psw)
            data.save()
            return redirect(login)
        #dont forget to make migration and migrate
        
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        name=request.POST['uname']
        psw=request.POST['password']
        user=auth.authenticate(username=name,password=psw)
        if user is not None:
            auth.login(request,user)
            return redirect(index)
        # else:
        #     return redirect(login)
    return render(request,'login.html')

def index(request):
    # if request.user.is_authenticated:
        # context={'user':request.user}

        return render(request,'index.html')#,{'value':context})

    # else:
    #     return redirect(login)

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect(login)
    else:
        return redirect(login)
    
def add_to_cart(request,product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_detail')

def cart_detail(request):
    if request.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        total = sum(item.total_price() for item in cart_items)
        
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})


def remove_from_cart(request, item_id):
    if request.user.is_authenticated:
        cart_item = get_object_or_404(CartItem, id=item_id)
        cart_item.delete()
        return redirect('cart_detail')
