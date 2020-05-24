# -*- coding: utf-8 -*-
"""
Created on Mon May 18 11:32:47 2020

@author: 470395
"""

'''
from django import forms
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User

'''
from django import forms
from blog.models import Post,Comment

class PostForm(forms.ModelForm):
    
    class Meta():
        model = Post
        fields = ('author','title','text')
        
        widgets = {
                'title': forms.TextInput(attrs={'class':'textinputclass'}),
                'text' : forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})}

class CommentForm(forms.ModelForm):
    
    class Meta():
        model = Comment
        fields = ('author','text')
        
        widgets = {
                'author': forms.TextInput(attrs={'class':'textinputclass'}),
                'text' : forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
                }