from django.urls import path
from main import views

urlpatterns = [
    # Визнач тут свої URL-шляхи
    path('profile-create/', views.ProfileCreateView.as_view(), name='profile-create'),
    path('profile-list/', views.ProfileListView.as_view(), name="profile-list")
]
app_name = "main"