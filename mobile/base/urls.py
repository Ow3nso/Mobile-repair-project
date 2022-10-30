from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('devices', views.device, name="device"),
    path('view/<deviceid>', views.view, name="view"),
    path('addservice', views.addserv, name='addserv'),
    path('adddev', views.adddev, name="adddev"),
    path('cart', views.cart, name='cart'),
    path('service', views.enquire, name='service'),
    path('logout', views.logout_user, name="logout"),
    path('login', views.login_user, name='login'),
    path('register', views.register, name='register'),
    path('navbar', views.navbar, name='navbar'),
    path('dele/<servid>', views.delserv, name="delserv"),
    path('del/<devid>', views.deldevice, name="deldevice"),
    path('update/<deviceid>', views.update, name="update"),

]