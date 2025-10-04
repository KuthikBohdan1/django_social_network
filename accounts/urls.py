from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.CustomRegisterView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustmLogoutView.as_view(), name='logout'),
]


# urlpatterns = [
#     path('register/', views.RegisterView.as_view(), name='register'),
#     path('login/', views.CustomLoginView.as_view(), name='login'),
#     path('logout/', views.CustomLogoutView.as_view(), name='logout'),
# ]