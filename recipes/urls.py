from django.urls import path

import recipes.views as recipes_views

app_name = "recipes"

urlpatterns = [
    path("recipes/category/<int:pk>/", recipes_views.category, name="category"),
    path("detail/<int:pk>/", recipes_views.detail, name="detail"),
    path("recipes/search", recipes_views.search, name="search"),
    path("", recipes_views.index, name="index"),
]
