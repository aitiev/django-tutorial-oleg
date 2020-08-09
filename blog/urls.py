from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_list, name='posts-list'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post-detail'),
    path('tags/', tags_list, name='tags-list'),
    path('tag/create/', TagCreate.as_view(), name='tag-create'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag-detail'),
]