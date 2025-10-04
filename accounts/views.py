from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from accounts.forms import RegisterForm, LoginForm
from accounts.models import CustomUser

class CustomRegisterView(CreateView):
    model = CustomUser
    form_class = RegisterForm
    template_name = "custom_accounts/register.html"
    success_url = reverse_lazy('login')

class CustomLoginView(LoginView):
    template_name = "custom_accounts/login.html"
    form_class = LoginForm
    redirect_authenticated_user = True

class CustmLogoutView(LogoutView):
    next_page = reverse_lazy('login')

# class CustomLogoutView(LogoutView):
#     pass

# class CustomLoginView(LoginView):
#     template_name = 'accounts/login.html'
#     redirect_authenticated_user = True
#     form_class = LoginForm


# class CustomLogoutView(LogoutView):
#     next_page = reverse_lazy('login')


# class RegisterView(CreateView):
#     model = User
#     template_name = 'accounts/register.html'
#     form_class = RegisterForm
#     success_url = reverse_lazy('login')
