from django.urls import path
from .views import *

app_name = 'user'

urlpatterns=  [
    path('profile/edit/',ProfileEditView.as_view(),name='profile_edit'),
    path('profile/list/',ProfileListView.as_view(),name='profile_list'),
    path('profile/detail/<int:pk>/',ProfileDetailView.as_view(),name='profile_detail'),
]