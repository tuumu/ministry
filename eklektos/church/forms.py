from .models import *
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

class WhatForm(forms.ModelForm):
    class Meta:
        model = Whatusay
        fields = ('name', 'email', 'body')

class SermonForm(forms.ModelForm):
    class Meta:
        model = Sermonsay
        fields = ('name', 'body')