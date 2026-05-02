from django.urls import path
from . import views

urlpatterns = [
    path("", views.RecipeListView.as_view()),
    path("create/", views.RecipeCreate),
    path("edit/", views.RecipeUpdate),
    path("delete/", views.RecipeDelete),
    path("photo/<str:id>/", views.get_photo),
]
    