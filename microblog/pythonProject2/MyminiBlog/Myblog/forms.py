from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Post, Comments
from django.contrib.auth.models import User
from datetime import date

class PostForm(forms.ModelForm):
    data = forms.DateField(initial=date.today)

    class Meta:
        model = Post
        fields = ['title', 'description', 'data', 'img']

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['email', 'name', 'text_comments']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    pass