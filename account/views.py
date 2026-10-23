from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView
from .forms import *
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

class RegisterView(CreateView):
    form_class = UserRgisterationForm
    template_name = 'account/registration.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect ('/')
        
        return super().dispatch(request, *args, **kwargs)

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'account/login.html'
    success_url  = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect ('/')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.cleaned_data.get('user')
        
        if user is not None:
            login(self.request,user)
            return super().form_valid(form)
        
        return super.form_invalid(form)

@login_required(login_url='/account/login.html/')
def logout_view(request):
    logout(request)
    return redirect('/')