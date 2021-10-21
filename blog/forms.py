from django import forms
from .models import Comment , Blog

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'blog_detail','image','blog_type','blog_description',]

