from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Post, MediaPost, CommentPost, PostReaction, Group, GroupMessage, GroupReactionMessage, GroupUser, Profile
from main.models import CustomUser
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from main.forms import ProfileForm, PostForm, CommentPostForm
from django.http import HttpResponse
from time import sleep
from django.core.paginator import Paginator
import json
from django.http import JsonResponse
from main.serializers import GroupMessageSerializer, structurator
# Create your views here.

async def ajaxInversed(request):
    print("2")
    return HttpResponse("s")

def ajaxLoadData(request):
    print("виконується функція ajaxLoadGroupGessages")
    id = request.GET.get("id")
    # data = GroupMessage.objects.filter(group__id = id).values_list('message', flat=True)
    # data = list(data)##це допомагає при боротьбі з query set
    messages = GroupMessage.objects.filter(group__id = id)
    serializer = GroupMessageSerializer(messages, many=True)
    result = structurator(group_id=1)
    result_json = json.dumps(result, ensure_ascii=False, indent=4)
    print(f'зібраний чат {result_json}')
    return JsonResponse({
        "message": serializer.data,
        "result": result_json,
    })

def SeeSroc(request, **kwargs):
    result = structurator(group_id=kwargs.get("id"))
    print(result)
    context = {
        "result":result,
    }
    return render(request, "see_stoctur/chat.html", context)

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
    def ajax_request(request):
        return HttpResponse("Дані отримано успішно!")
    
class CommentPostCreateView(LoginRequiredMixin, CreateView):
    model = CommentPost
    template_name = "posts/comment_post.html"
    form_class = CommentPostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = CommentPost.objects.filter(post_id=self.kwargs.get("post_id"))
        context["id"] = self.kwargs.get("post_id")
        return context
    
    def get_success_url(self, **kwargs):
        return reverse_lazy("main:comments-post", kwargs = {'post_id': self.kwargs.get("post_id")})

    def form_valid(self, form, **kwargs):
        print(self.request.user)
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, id=self.kwargs.get("post_id"))
        valid = super().form_valid(form)
        return valid
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

class HomeListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "main/main_page.html"
    context_object_name = "posts"
    paginate_by = 1

    def get(self, request):
        super().get(request)
        if request.headers.get('x-requested-width') == 'XMLHtppsRequest':
            return render(request, 'polls/list.html', context=self.get_context_data())
        return render(request, self.template_name, context=self.get_context_data())
    

class GroupListView(LoginRequiredMixin, ListView):
    model = Group
    template_name = "group/group_list.html"
    context_object_name = "groups"
    
    def get_queryset(self):
        return super().get_queryset()
