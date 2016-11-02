#!/usr/bin/python
#coding=utf-8

from django.conf.urls.static import static
from django.conf.urls import *
from books.views import *
urlpatterns=[
        url('^book/$',book_page),
        url('^index2/$',static_index),
        ]
