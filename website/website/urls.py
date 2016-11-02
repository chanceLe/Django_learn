"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from views import *
#from books.views import *
from contact.views import *
from django.conf import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^index/$',page),
    url('^books/',include('books.urls')),
  #  url('^book/$',book_page),
 #   url('^search-form/$',search_form),
  #  url('^search-form1/$',search_form1),
   # url('^search1/$',search1),
    #url('^search/$',search),
    #contanctform
    url('^contact/$',contact),
    url('^contactsend/$',contactsend),
    #manytoone
    url('^foo/$',foo_bar,{'template_name':'template.html'}),
    url('^bar/$',foo_bar,{'template_name':'template1.html'}),
]
