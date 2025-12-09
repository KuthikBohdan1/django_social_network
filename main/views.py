from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Post, MediaPost, CommentPost, PostReaction, Group, GroupMessage, GroupReactionMessage, GroupUser, Profile
from main.models import CustomUser
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from main.forms import ProfileForm, PostForm, CommentPostForm, GroupMessageForm, GroupForm, GroupUserForm
from django.http import HttpResponse
from time import sleep
from django.core.paginator import Paginator
import json
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from django.http import JsonResponse
from main.serializers import GroupMessageSerializer, structurator, PostSerializer, GroupMessageSerializer
# Create your views here.
class Group_id:
    def __init__(self):
        self.value = None
group_id = Group_id()

async def ajaxInversed(request):
    return HttpResponse("s")

async def ajaxPostLike(request):
    pass

@api_view(['POST'])
def toggle_like(request, post_id):
    """
    API endpoint для додавання/видалення лайку
    POST /api/posts/{post_id}/toggle-like/
    """
    # Отримуємо пост
    print(post_id)
    post = get_object_or_404(Post, id=post_id)
    user = get_object_or_404(CustomUser, email=request.user)
    print(user)
    reaction_exist = PostReaction.objects.filter(post=post, user=user, reaction='like').exists()
    if reaction_exist:
        PostReaction.objects.filter(post=post, user=user, reaction='like').delete()
        liked = False
        post.like_fast -= 1 
        post.save()
    else:
        PostReaction.objects.create(post=post, user=user, reaction='like')
        liked = True
        post.like_fast += 1
        post.save()

    return Response({
        'liked': liked,
        'likes_count': post.like_fast,
    })


def ajaxLoadData(request, id=None):
    print("виконується функція ajaxLoadGroupGessages")
    if request.GET.get("id"):
        id = request.GET.get("id")
        print(id)
    group_id.value = id
    group = get_object_or_404(Group, id = id)
    messages = GroupMessage.objects.filter(group__id = id)
    serializer = GroupMessageSerializer(messages, many=True)
    if group.image_group:
        avatar = group.image_group.url
    else:
        avatar = None
    if group.type == "forum":
        type = Group.objects.get(id = id)
        result = structurator(group_id=id, type=type.type)
    elif group.type == "chat":
        print(serializer.data)
        result = {
            "type": "chat",
            "group_id": group.id,
            "name": group.name,
            "avatar":avatar,
            "messages": serializer.data,
        }
    request.session["last_chat"] = id
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

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = "profiles/profile_update.html"
    form_class = ProfileForm
    success_url = reverse_lazy("main:profile-list")

    def get_object(self, queryset=None):
        user = self.request.user
        print(f"user{user}")
        return get_object_or_404(Profile, user__email = user)
    
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
    template_name = "main/main_page_old.html"
    context_object_name = "post"
    paginate_by = 3
    serializer_class = PostSerializer
    
class PostPagination(PageNumberPagination):
    page_size = 3  # Кількість постів на сторінці
    page_size_query_param = 'page_size'  # Параметр для зміни розміру сторінки
    max_page_size = 50  # Максимальний розмір сторінки
    
class PostListAPiView(generics.ListAPIView):
    queryset = Post.objects.filter()
    serializer_class = PostSerializer
    pagination_class = PostPagination

    def get_queryset(self):
        queryset = super().get_queryset()    
        return queryset

def posts_list_view(request):
    context = {
        'page_title': 'Список постів',
        'api_url': '/api/posts/',  # URL для API запитів
    }
    return render(request, 'home/posts_list.html', context)

class GroupListView(LoginRequiredMixin, ListView):
    model = Group
    template_name = "group/group_list.html"
    context_object_name = "groups"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        last_group_id = self.request.GET.get("last_chat")
        if last_group_id:
            context["last_group_id"] = last_group_id

        context["form"] = GroupMessageForm()
        query = self.request.GET.get('q', '')
        if query:
            groups = Group.objects.filter(name__icontains = query)
            print(groups)
            context["groups"] = groups
        return context

    def post(self, request, *args, **kwargs):
        form = GroupMessageForm(request.POST)
        if form.is_valid():
            print(group_id.value)
            form.instance.group = Group.objects.get(id = group_id.value)
            form.instance.user = CustomUser.objects.get(id = request.user.id)
            parent_id = request.POST.get("reply")
            print(f"parent_id {parent_id}")
            if parent_id:
                form.instance.parent = GroupMessage.objects.get(id=parent_id)
            form.save()
            return redirect("main:group")
        else:
            return redirect("main:group")        

    def get_queryset(self):
        queryset = GroupUser.objects.filter(user = self.request.user).values_list("group__id", flat=True)
        return Group.objects.filter(id__in = queryset)

class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    template_name = "group/group_create.html"
    form_class = GroupForm
    success_url = reverse_lazy("main:group")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        obj = form.save(commit=True)
        print(f"obj{obj.id}")
        GroupUser.objects.create(user = self.request.user, group = obj)
        return super().form_valid(form)

class GroupUserCrete(LoginRequiredMixin, CreateView):
    model = GroupUser
    template_name  = "group_user/create_group_user.html"
    form_class = GroupUserForm