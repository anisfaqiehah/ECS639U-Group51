import email
from rest_framework.response import Response
from rest_framework import status
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
from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import User, Bid, Item, ItemComment,  ItemCategory, AuctionHistory
from .utils import utility
import json 
from rest_framework import viewsets
from .forms import RegisterForm,LoginForm
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from .serializer import ItemSerializer ,ProfileSerializer,CommentSerializer
from rest_framework.authentication import TokenAuthentication

def register_view(request):
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
                return render(request, 'frontpage.html',{'page': 'frontpage'})

    return render(request, 'register.html', {'form': form})



def login_view(request):
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
                #return redirect('indexview')
                return render(request, 'frontpage.html',{'page': 'frontpage'})

            # failed authentication
            form.add_error('username', 'Invalid credentials')
            form.add_error('password', 'Invalid credentials')
            return render(request, 'login.html', {'form': form})

    return render(request, 'login.html', {'form': form})




def indexview(request):

      return render(request, 'base.html',{'page': 'frontpage'})


def logoutView(request):
      return redirect("frontpage")



@api_view(['GET','POST'])
def items_view(request:HttpRequest)-> HttpResponse:
      if request.method=='GET':
            return JsonResponse({
            'items': [
                item.to_dict()
                for item in Item.objects.all()
            ]
        })
      """""
      if request.method=='POST':
            serializer=ItemSerializer(data=request.data)
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data, status==status.HTTP_201_CREATED)
"""
      

@api_view(['GET'])
def profile_view(request:HttpRequest)-> HttpResponse:
       if request.method=='GET':
             
            return JsonResponse({
            'profiles': [
                profile.to_dict()
                for profile in User.objects.all()
            ]})
            
      



@api_view(['GET','PUT','DELETE'])
def profile_detail(request,id):

      try:
            profile= User.objects.get(pk=id)
      except User.DoesNotExist:
            return Response(status==status.HTTP_404_NOT_FOUND)

      if request.method=='GET':
            serializer=ProfileSerializer(profile)
            return Response(serializer.data)
      elif request.method=='PUT':
            serializer=ProfileSerializer(profile,data=request.data)
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      elif request.method=='DELETE':
            profile.delete()
            return Response(status=status.HTTP_200_OK)


@api_view(['GET','PUT','DELETE'])
def item_detail(request,id):

      try:
            item= Item.objects.get(pk=id)
      except Item.DoesNotExist:
            return Response(status==status.HTTP_404_NOT_FOUND)

      if request.method=='GET':
            serializer=ItemSerializer(item)
            return Response(serializer.data)
      elif request.method=='PUT':
            serializer=ItemSerializer(item,data=request.data)
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      elif request.method=='DELETE':
            item.delete()
            return Response(status=status.HTTP_200_OK)
            

def comment_view(request):
      pass


@api_view(['GET'])
def comment_view(request,id):
      item= Item.objects.get(pk=id)
      #itemName= Item.objects.filter(title="laptop").get()
      if request.method=='GET':
            what_item=Item.objects.filter(title=item.title).get()
            return JsonResponse({
            'comments': [
                comment.to_dict()
                for comment in ItemComment.objects.filter(item= what_item)
            ]
        })
    
@api_view(['POST'])
def add_comment(request):
    #Verify and recover the text
      if request.method == 'POST':
            serializer=CommentSerializer(data=request.data)
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data, status==status.HTTP_201_CREATED)

            """""
            item_name = request.POST.get('item')
            comment = str(request.POST.get('text'))
            item_obj = Item.objects.filter(title=item_name)
            #author = User.objects.filter(username = request.user.username).get()
            new_comment = ItemComment(text=comment,  item=item_obj)
            new_comment.save()    
      return Response(new_comment, status==status.HTTP_201_CREATED)
   """
     
    