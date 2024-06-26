from django.contrib import admin
from .models import Post, Comments
from .forms import PostForm, CommentsForm

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ('title', 'author', 'data')

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    form = CommentsForm
    list_display = ('name', 'email', 'post')