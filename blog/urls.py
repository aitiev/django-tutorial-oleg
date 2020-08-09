from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_list, name='posts-list'),
    path('post/create/', PostCreate.as_view(), name='post-create'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post-detail'),
    path('post/<str:slug>/update/', PostUpdate.as_view(), name='post-update'),
    path('post/<str:slug>/delete/', PostDelete.as_view(), name='post-delete'),
    path('tags/', tags_list, name='tags-list'),
    path('tag/create/', TagCreate.as_view(), name='tag-create'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag-detail'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag-update'),
    path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tag-delete'),
]