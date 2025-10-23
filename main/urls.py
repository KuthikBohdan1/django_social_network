from django.urls import path
from main import views

urlpatterns = [
    # Визнач тут свої URL-шляхи
    path('profile-create/', views.ProfileCreateView.as_view(), name='profile-create'),
    path('profile-list/', views.ProfileListView.as_view(), name="profile-list"),
    path('post-create/', views.PostCreateView.as_view(), name="post-create"),
    path('post-detail<int:pk>', views.PostDetailView.as_view(), name="post-detail"),
    path('comments-post<int:post_id>',views.CommentPostCreateView.as_view(), name="comments-post"),
    path('home/', views.HomeListView.as_view(), name="home"),
    path('ajax_request/',views.ajax_request, name="ajax_request"),
    path('ajax-inversed/',views.ajaxInversed, name="ajax-inversed"),
]
app_name = "main"