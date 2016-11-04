#!/usr/bin/python
#coding=utf-8

from django.conf.urls import *
from views import *
urlpatterns=[ 
    url('^login/$',login),
    url('^register/$',regis),
    url('^check/$',check),
    url('^haslogin/$',haslogin),
    url('^login_check/$',login_check),
    url('^writearticle/$',writearticle),
    url('^publish/$',publish),
    url('^(\d+?)/$',showarticle),

        ]
