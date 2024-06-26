from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from .models import Post
from .forms import CommentsForm, PostForm, CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from faker import Faker



class PostView(View):
    '''Вывод записи'''

    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/blog.html', {'post_list': posts})


class PostDetail(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentsForm()
        return render(request, 'blog/blog_detail.html', {'post': post, 'form': form})


class PostEdit(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'post': post, 'form': form})


class AddComments(View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        form = CommentsForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post_id)
        return redirect(f'/{post_id}')


class AddPost(View):
    @method_decorator(login_required)
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/add_post.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
        return render(request, 'blog/add_post.html', {'form': form})


class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'blog/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('login')
        return render(request, 'blog/register.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = CustomAuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request):
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Неверный Логин или пароль')
        return render(request, 'registration/login.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


@method_decorator(login_required, name='dispatch')
class PostEditView(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        if request.user == post.author:
            form = PostForm(instance=post)
            return render(request, 'blog/post_edit.html', {'form': form, 'post': post})
        else:
            messages.error(request, 'Вы не авторизованы для редактирования этого поста')
            return redirect('post_detail', pk=post_id)


def post(self, request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.author:
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post.author = request.user
            form.save()
            messages.success(request, 'Пост успешно отредактирован')
            return redirect('post_detail', pk=post.id)
        return render(request, 'blog/post_edit.html', {'form': form, 'post': post})
    else:
        messages.error(request, 'Вы не авторизованы для редактирования этого поста')
        return redirect('post_detail', pk=post_id)


@method_decorator(login_required, name='dispatch')
class PostDeleteView(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        if request.user == post.author:
            post.delete()
            messages.success(request, 'Пост успешно удален')
            return redirect('/')
        else:
            messages.error(request, 'Вы не авторизованы для удаления этого поста')
        return redirect('post_detail', pk=post_id)

