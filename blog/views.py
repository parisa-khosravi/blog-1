from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *


class postList(ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(status=True).select_related('author').prefetch_related('category')
    paginate_by =2

class PostDetail(DetailView):   
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    queryset = Post.objects.filter(status=True).select_related('author').prefetch_related('category')

class PostCreate(LoginRequiredMixin,CreateView):
    template_name = 'blog/post_create.html'
    form_class = 'PostForm'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)