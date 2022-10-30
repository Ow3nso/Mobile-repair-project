from dataclasses import fields

from django.forms import ImageField, ModelForm, TextInput, EmailInput, IntegerField

from django import forms
from flask import request
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = "__all__"

class DeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = "__all__"

class EnquireForm(ModelForm):
    class Meta:
        model = Enquiry
        fields = "__all__"
        widgets = {
            'firstname': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'First Name'
                }),
            'secondname': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Second Name'
                }),
            'phonenumber': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Phone Number'
                }),
            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                }),
            'phonetype': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Phone Type'
                }),
            'damage': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Type of Damage'
                }),
            'description': forms.Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Damage description'
                }),
        }

class Registerform(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username','email', 'password1','password2')