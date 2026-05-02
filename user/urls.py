from django.urls import path
from . import views

urlpatterns = [
    path("profile/", views.perfil),
    path('register/', views.UserRegisterView.as_view(), name='user-register'),
    path('', views.UserListView.as_view(), name='user-list'),
    path('<int:pk>/', views.UserUpdateView.as_view(), name='user-update'),
    path('<int:pk>/', views.UserDeleteView.as_view(), name='user-delete'),
]
