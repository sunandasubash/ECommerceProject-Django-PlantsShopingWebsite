from django.contrib import auth, messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from shop.models import Category,Products
from django.core.paginator import Paginator,EmptyPage,InvalidPage


# Create your views here.
def allProdCat(request,c_slug=None):
    c_page=None
    products_list=None
    categories = Category.objects.all() # edited

    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        products_list=Products.objects.all().filter(category=c_page,available=True)
    else:
        products_list=Products.objects.all().filter(available=True)

    paginator=Paginator(products_list,8)
    try:
        page=int(request.GET.get('page',1))
    except:
        page=1
    try:
        products = paginator.page(page)
    except (EmptyPage,InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request,'category.html',{'category':c_page,'products':products,'categories': categories})

def prodDetail(request,c_slug,product_slug):
    try:
        product=Products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})

# user login logout and register functions

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/shop')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method =='POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['con_password']
        if password == confirm:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exist")
                return redirect('shop/register')
            elif User.objects.filter(email= email).exists():
                messages.info(request,"Emailid already exist")
                return redirect('shop/register')
            else:
                user = User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email)
                user.save();
        else:
            messages.info(request,"Password is not matched")
            return redirect('register')
        return redirect('/shop')

    return render(request,'register.html')


def user_logout(request):
    logout(request)
    return redirect('shop:allProdCat')
