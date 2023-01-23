from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from store.models import Product

def index(request):
    products = Product.objects.filter(status=Product.ACTIVE)[0:6]
    return render(request, 'online_site/index.html', {'products':products})


def cart(request):
    return render(request, "online_site/cart.html", {})

def contact(request):
    return render(request, "online_site/contact.html", {})

def detail(request):
    return render(request, "online_site/detail.html", {})

def shop(request):
    return render(request, "online_site/shop.html", {})