from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post, Comment

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ["poster", 'post_time', 'posterip', 'viewersip']


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ["poster", 'post_time', 'posterip', 'viewersip']

    
class CommentCreationForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
