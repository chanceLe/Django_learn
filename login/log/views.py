# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from django.shortcuts import render,render_to_response

from log import models
# Create your views here.

def login(request):
    return render_to_response('login.html',{})
def login_check(request):
    errors=[]
    name=request.GET['user']
    password=request.GET['password']
    if password == models.Users.objects.filter(user=name)[0].password:
        return render_to_response('haslogin.html',{'name':name})
    else:
        return render_to_response("login.html",{'error':"user or password is wrong.Please try again"})


def check(request):
    errors=[]
    name=request.GET['user']
    password=request.GET['password']
    gender=request.GET['gender']
    email=request.GET['email']
    try:
        models.Users.objects.get(user=name)
        errors.append("Username has been exist.")
        return render_to_response("regis.html",{'errors':errors})
    except ObjectDoesNotExist:
        pass

    if not password:
        errors.append("password is must.")
        return render_to_response("regis.html",{'errors':errors})
    elif len(password)<8:
        errors.append("password at least 8 bit code.")
        return render_to_response("regis.html",{'errors':errors})
    else:
        p=models.Users(user=name,password=password,gender=gender,email=email)
        p.save()
        return render_to_response('login.html',{}) 



def regis(request):
    return render_to_response('regis.html',{})
def haslogin(request):
    return render_to_response('haslogin.html',{'name':user})
