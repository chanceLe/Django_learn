#!/usr/bin/python
#coding=utf-8

from django.conf.urls.static import static
from django.conf.urls import *
#通用视图TemplateView
from django.views.generic import TemplateView
from books.views import *

#通用视图ListView
from django.views.generic.list import ListView
from books.models import Book

urlpatterns=[
        url('^book/$',book_page),
        url('^index2/$',static_index),
        url('^template/$',TemplateView.as_view(template_name='index2.html')),
        url(r'list/$',ListView.as_view(model=Book,template_name="book_show.html"))
        ]
