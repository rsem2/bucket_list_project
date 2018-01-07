# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import User
from django.contrib import messages

# Create your views here.
def index(request):
    if 'userid' not in request.session:
        request.session['userid'] = None
    elif request.session['userid'] != None:
        return redirect('/dashboard')
    return render(request,'index.html')

def register(request):
    results = User.objects.registerVal(request.POST)
    if results['status'] == True:
        for error in results['errors']:
            messages.error(request, error)
    else:
        User.objects.createUser(request.POST)
        messages.success(request, "Your user has been created. Please login.")   
    return redirect('/')

def login(request):
    results = User.objects.loginVal(request.POST)
    if results['status'] == True:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['first_name'] = results['user'].first_name
        request.session['userid'] = results['user'].id
        request.session['email'] = results['user'].email
        return redirect('/dashboard')

def logout(request):
    request.session.flush()
    return redirect('/')