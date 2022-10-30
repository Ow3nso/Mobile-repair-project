from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    
    service = Service.objects.all()
    context = {'service':service}

    return render(request, 'home.html', context)

@login_required(login_url='login')
def device(request):

    device = Device.objects.all()
    context = {'device':device}

    return render(request, 'device.html', context)

@login_required(login_url='login')
def view(request, deviceid):

    device = Device.objects.get(pk=deviceid)

    context = {'device':device}

    return render(request, 'view.html', context)

@login_required(login_url='login')

def addserv(request):

    form = ServiceForm

    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('/')

    context = {'form':form}


    return render(request, 'addserv.html', context)

@login_required(login_url='login')
def adddev(request):
    form = DeviceForm

    if request.method =="POST":
        form = DeviceForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            
            return redirect('/')

    context = {'form':form}

    return render(request, 'add-device.html', context)

@login_required(login_url='login')
def cart (request):

    user = request.user
    cart = Cart.objects.filter(user=user)
    total_cart = cart.count()

    if request.method == "POST":
        id = request.POST.get('id')
        name = request.POST.get('name')
        qnty = request.POST.get('qnty')
        price = request.POST.get('price')

        
        user = request.user
        x = Cart(user=user, id=id, name=name,price=price)
        messages.success('item added to cart Successfully')
        x.save()

    context = {'cart':cart, 'total_cart':total_cart}

    return render(request, 'cart.html', context)

@login_required(login_url='login')
def service(request):

    return render(request, 'service.html')


def logout_user(request):

    logout(request)

    return redirect('/')

def login_user(request):

    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("Invalid username or password"))
            return redirect('login')

    else:

        return render(request, 'login.html')

def register(request):

    form = Registerform

    if request.method=="POST":
        form = Registerform(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password1')
            user = authenticate(username=username, email=email, password=password)
            messages.success(request, ("Registration successful. Please Login"))
            return redirect('login')
        else:
            messages.success(request, 'Registration not Successfull')
            return redirect('register')

    else:
        form = Registerform()


    context = {'form':form}

    return render(request, 'register.html', context)

def navbar(request):

    user=request.user

    cart = Cart.objects.filter(user=user)

    total_cart = cart.count()

    context = {'total_cart':total_cart}
    return render(request, 'navbar.html', context)


def delserv(request, servid):

    serv = Service.objects.get(pk=servid)
    serv.delete()
    return redirect('/')

def deldevice(request, devid):

    device =Device.objects.get(pk=devid)
    device.delete()

    return redirect('device')

def update(request, deviceid):

    device = Device.objects.get(pk=deviceid)
    form = DeviceForm(request.POST or None, instance=device)

    if request.POST == "POST":
        if form.is_valid():
            form.save()
            return redirect('/')

    context= {'form':form, 'device':device}
    return render (request, 'update.html', context)


def enquire(request):
    
    form = EnquireForm
    if request.method == "POST":
        form = EnquireForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Enquiry Sent Successfully')
        return redirect('/')
    context = {'form':form}

    return render(request, 'service.html', context)