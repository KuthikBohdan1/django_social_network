from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .models import Post, MediaPost, CommentPost, PostReaction, Group, GroupMessage, GroupReactionMessage, GroupUser, Profile
from main.models import CustomUser
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from main.forms import ProfileForm, PostForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = Post.objects.filter(profile__user = self.request.user)
        # context["photo_card"] = MediaPost.objects.filter()
        return context

    def get_queryset(self):
        context = super().get_queryset()
        print(self.request.user)
        context = Profile.objects.filter(
            user_id__email = self.request.user
        )
        return context

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["post_id"] = self.kwargs["pk"]
        return context

class CommentPostCreateView(LoginRequiredMixin, CreateView):
    model = CommentPost
    template_name = "posts/comment_post.html"

    def get_context_data(self, **kwargs):
        context = super(CommentPostCreateView, self).get_context_data(**kwargs)
        context = Post.objects.filter()
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/post_create.html"
    success_url = reverse_lazy("main:post-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['MediaPostForm'] = MediaPostForm
        return context
    
    def get_success_url(self):
        return super().get_success_url()
    
    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        post = super().form_valid(form)
        files = self.request.FILES.getlist('media')
    
        for file in files:
            MediaPost.objects.create(post = self.object, media = file)
        return post

class MainListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "main_page/houme.html"
    form_class = 

# class MediaPostCreateView(LoginRequiredMixin, CreateView):
#     model = MediaPost
#     form_class = MediaPostForm
#     template_name = ""