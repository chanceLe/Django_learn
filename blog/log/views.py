# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from time import ctime

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
    articles=models.Articles.objects.all()
    try:
        if password == models.Users.objects.filter(user=name)[0].password:
            global username
            username=name
            return render_to_response('first_page.html',{'name':username,'articles':articles})
        else:
            return render_to_response("login.html",{'error':"user or password is wrong.Please try again"})
    except IndexError :
            return render_to_response("login.html",{'error':"You must enter user and password.Please try again"})


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
    articles=models.Articles.objects.all()
    return render_to_response('first_page.html',{'name':username,'articles':articles})

def writearticle(request):
    return render_to_response('writearticle.html')

def publish(request):
    title=request.GET['title']
    author=request.GET['author']
    text=request.GET['text']
    if not title:
        title=ctime()
    if not author:
        author=username
    a=models.Articles(title=title,author=author,time=ctime(),text=text,discuss="well")
    a.save()
    return render_to_response('writearticle.html',{'publish':'Publish OK!'})
def showarticle(request,idnum):
    article=models.Articles.objects.get(id=idnum)
    return render_to_response('showarticle.html',{'article':article})
