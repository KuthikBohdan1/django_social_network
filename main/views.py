from django.shortcuts import render, redirect
from .models import Post, Post_reaction, Group, Group_message, Group_Reaction_message, Group_users, Profile
from main.models import CustomUser
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from main.forms import ProfileForm
# Create your views here.


class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    template_name = "profiles/profie_create.html"
    form_class = ProfileForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        if Profile.objects.filter(user = self.request.user).exists(): ##exist перевіряє чи є такий обєкт та повертає true fals
            return redirect('profile-list')
        form.instance.user = self.request.user
        valid = super().form_valid(form)
        return valid

class ProfileListVIew(LoginRequiredMixin, ListView):
    model = Profile
    template_name = "profiles/profile_list.html"
    context_object_name = "profiles"

    def get_queryset(self):
        context = super().get_queryset()
        return context