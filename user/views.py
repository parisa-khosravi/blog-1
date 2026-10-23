from django.shortcuts import render
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView,ListView,DetailView
from django.urls import reverse_lazy

class ProfileEditView(LoginRequiredMixin,UpdateView):
    
    form_class = ProfileForm
    template_name = 'user/profile_edit.html'
    login_url = 'account/login/'
    success_url = reverse_lazy('user:profile_edit')

    def get_object(self, queryset = None):
        return self.request.user.profile

class ProfileListView(ListView):

    queryset = Profile.objects.filter(user__is_active=True)
    template_name = 'user/profile_list.html'
    context_object_name = 'profiles'

class ProfileDetailView(DetailView):

    queryset = Profile.objects.all()  ##or model=profile
    template_name = 'user/profile_detail.html'
    context_object_name = 'profile'
