from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login

def signup(request):
    if request.user.is_authenticated:
        return redirect('/products')
    if request.method=="POST":
        signup_form=SignupForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return redirect('/products')
    else:
        signup_form=SignupForm()
    return render(request, "signup.html", {'signup_form': signup_form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/products')
    error=None
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/products')
        else:
            error="Invalid username or password"
    return render(request, "login.html", {"error": error})

