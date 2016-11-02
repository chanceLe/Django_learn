#!/usr/bin/python
#coding=utf-8

from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required = False,label="Your email address")  #括号参数表示此项可以缺省。
    message = forms.CharField(widget=forms.Textarea)

'''
    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError('Not enough words.')
        return message
'''
