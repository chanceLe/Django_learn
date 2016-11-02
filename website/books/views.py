#coding=utf-8
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import HttpResponse

from django.template import loader
from books import models

# Create your views here.

def book_page(request):
    #取出指定字段所有值
    #name_list=models.Publisher.objects.values('name',"city")
    #get查找，只能查询一条数据
    #name_list=models.Publisher.objects.get(id=1)
    
    #修改数据，改完再获取
    #models.Publisher.objects.filter(id=1).update(city="chengdu")
    #name_list=models.Publisher.objects.get(id=1)

    #修改数据，获取后再改。
    #name_list=models.Publisher.objects.get(id=1)
    #name_list.city="guangzhou"
    #name_list.save()

    #删除数据,找不到，会抛出 Publisher matching query does not exist。
    #models.Publisher.objects.filter(id=2).delete()
    name_list=models.Publisher.objects.get(id=1)

    #name_list=models.Publisher.objects.all()
    #name_list=[{'name':'zhangsan','city':'beijing'},{'name':'lisi','city':'shanghai'}]
    return render_to_response('show.html',{'name_list':name_list})


def search_form(request):
    return render_to_response('form.html',{})

def search(request):
    if 'name' in request.GET and request.GET['name']:
        name=request.GET['name']
        books=models.Book.objects.filter(title__icontains=name)
        return render_to_response('search.html',{'books':books,'query':name})
    else:
        return render_to_response('form.html',{'error':True})

def search_form1(request):
    return render_to_response('form0.html',{})

def search1(request):
    errors=[]
    if 'name' in request.GET:
        name=request.GET['name']
        if not name:
            errors.append("Enter a content.")
        elif len(name)>20:
            errors.append("Please enter less than 20 code.")
        else:
            books=models.Book.objects.filter(title__icontains=name)
            return render_to_response('search.html',{'books':books,'query':name})
    
    return render_to_response('form0.html',{'errors':errors})

def static_index(request):
    return render_to_response('index2.html')
