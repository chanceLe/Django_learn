#coding=utf-8
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect #这个函数是页面跳转函数。
from contact.forms import ContactForm
# Create your views here.

def thanks(request):
    return HttpResponse("Thanks!")

def contactsend(request):
    return render_to_response("contact_form.html",{})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            text='''
            subject:%s\r\n
            message:%s\r\n
            '''%(cd['subject'],cd['message'])
            return HttpResponse(text)
    else:
        form=ContactForm()
    return render_to_response('contact_form1.html',{'form':form})

def foo_bar(request,template_name):
    return render_to_response(template_name,{'name':'Foo'})

