from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('post/',postList.as_view(),name='post_list'),
    path('post/<int:pk>/',PostDetail.as_view(),name='post_detail'),
    path('post/create/',PostCreate.as_view(),name='post_create'),
]