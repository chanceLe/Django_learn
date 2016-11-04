# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Users(models.Model):
    user = models.CharField(max_length = 30)
    password = models.CharField(max_length = 20)
    gender = models.CharField(max_length = 10)
    email = models.EmailField(max_length = 30)
    def __unicode__(self):
        return self.user

class Articles(models.Model):
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=10) 
    time = models.CharField(max_length=100)
    text=models.TextField()
    discuss = models.CharField(max_length=120)
    def __unicode__(self):
        return self.title


