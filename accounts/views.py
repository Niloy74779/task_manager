from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .forms import SignupForms
from django.urls import reverse_lazy

# Create your views here.

class UserSignupView(CreateView):
    form_class = SignupForms
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class UserLoginView(LoginView):
    template_name = 'login.html'
    
class UserLogoutView(LogoutView):
    next_page = 'home'







