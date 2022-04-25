from django import forms
from django.db.models import fields
from App_Posts.models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['image', 'caption', ]