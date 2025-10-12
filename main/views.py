from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .models import Post,Media_Post,Post_reaction, Group, Group_message, Group_Reaction_message, Group_users, Profile
from main.models import CustomUser
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from main.forms import ProfileForm, PostForm, Media_postForm
# Create your views here.


class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    template_name = "profiles/profie_create.html"
    form_class = ProfileForm
    
    def get_success_url(self):
        return reverse_lazy("main:profile-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        if Profile.objects.filter(user = self.request.user).exists(): ##exist перевіряє чи є такий обєкт та повертає true fals
            return redirect('main:profile-list')
        form.instance.user = self.request.user

        valid = super().form_valid(form)
        return valid

class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = "profiles/profile_list.html"
    context_object_name = "profiles"

    def get_queryset(self):
        context = super().get_queryset()
        print(self.request.user)
        context = Profile.objects.filter(
            user_id__email = self.request.user
        )
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/"

class Media_postCreateView(LoginRequiredMixin, CreateView):
    model = Media_Post
    form_class = Media_postForm
    template_name = ""