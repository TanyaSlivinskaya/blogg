from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

from .views import PostView, PostDetail, AddComments, AddPost, RegisterView, LoginView, LogoutView, PostEditView, \
    PostDeleteView
from django.conf import settings

urlpatterns = [
    path('', PostView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('review/<int:post_id>/', AddComments.as_view(), name='add_comments'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('post/<int:post_id>/edit/', PostEditView.as_view(), name='post_edit'),
    path('post/<int:post_id>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),


]
