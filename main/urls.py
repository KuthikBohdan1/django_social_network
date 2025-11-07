from django.urls import path
from main import views

urlpatterns = [
    # Визнач тут свої URL-шляхи
    path('profile-create/', views.ProfileCreateView.as_view(), name='profile-create'),
    path('profile-list/', views.ProfileListView.as_view(), name="profile-list"),
    path('post-create/', views.PostCreateView.as_view(), name="post-create"),
    path('post-detail<int:pk>', views.PostDetailView.as_view(), name="post-detail"),
    path('api/posts/', views.PostListAPiView.as_view(), name="posts_api_list"),
    path('home', views.posts_list_view, name='home'),
    path('hom/', views.HomeListView.as_view(), name='hom/'),
    path('group/', views.GroupListView.as_view(), name="group"),
    path('ajax-inversed/',views.ajaxInversed, name="ajax-inversed"),
    path('load-data/', views.ajaxLoadData, name="load_data"),
    path('see-<id>/', views.SeeSroc, name="see")
    ]
app_name = "main"