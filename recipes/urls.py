from django.urls import path

import recipes.views as recipes_views

app_name = "recipes"

urlpatterns = [
    path("", recipes_views.index, name="index"),
    path("create/", recipes_views.create, name="create"),
    path("detail/<int:pk>/", recipes_views.detail, name="detail"),
    path("edit/<int:pk>/", recipes_views.edit, name="edit"),
    path("delete/<int:pk>/", recipes_views.delete, name="delete"),
]
