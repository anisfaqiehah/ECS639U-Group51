import email
from types import CoroutineType
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django import forms
import logging
from django.db import models

from .models import User, Bid, Item, ItemComment, Watchlist, ItemCategory, AuctionHistory,UserProfile
from .utils import utility
import json 
from django.core import serializers
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm,LoginForm
from django.contrib.auth.decorators import login_required

def register(request):
    '''
    Signup function
    Users creating an account
    '''

    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']

            if not username:
                form.add_error('username', 'Please choose a username')
                return render(request, 'register.html', {'form': form})

            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Username already exists')
                return render(request, 'register.html', {'form': form})

            email= form.cleaned_data['email']
            if not email:
                form.add_error('email', 'Please choose an email')
                return render(request, 'register.html', {'form': form})

            if form.cleaned_data['password'] != form.cleaned_data['password_confirm']:
                form.add_error('password', 'Passwords do not match')
                form.add_error('password_confirm', 'Passwords do not match')
                return render(request, 'register.html', {'form': form})

            password = form.cleaned_data['password']
            
            # create a new user
            new_user = User.objects.create(username=username,email=email)
            # set user's password
            new_user.set_password(password)
            new_user.save()

            #email=form.cleaned_data['email']
            #city=form.cleaned_data['city']
            #new_profile=UserProfile.create(user=new_user,email=email,city=city)
           # new_profile.save()
            # authenticate user
            # establishes a session, will add user object as attribute
            # on request objects, for all subsequent requests until logout
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index.html')

    return render(request, 'register.html', {'form': RegisterForm})



def login(request):
    '''
    Login function
    Users logging into the app
    '''
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')

            # failed authentication
            form.add_error('username', 'Invalid credentials')
            form.add_error('password', 'Invalid credentials')
            return render(request, 'login.html', {'form': form})

    return render(request, 'login.html', {'form': form})



@login_required
def indexview(request):

      return render(request, 'index.html',{'page': 'index'})