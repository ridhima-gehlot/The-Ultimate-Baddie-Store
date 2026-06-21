from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

class SignupForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model= User
        fields=["username", "email", "password1", "password2"]

