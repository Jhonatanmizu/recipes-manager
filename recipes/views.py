from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Recipe


def get_recipe_or_404(pk: int | None = None) -> Recipe | list[Recipe]:
    if pk:
        recipe = get_object_or_404(Recipe, pk=pk, is_published=True)
        return recipe
    return get_list_or_404(Recipe, is_published=True)


def index(request: HttpRequest) -> HttpResponse:
    recipes = Recipe.objects.filter(is_published=True).order_by("-created_at")
    context = {"title": "Recipes", "recipes": recipes}
    return render(request, "recipes/pages/index.html", context)


def detail(request: HttpRequest, pk: int) -> HttpResponse:
    recipe = get_recipe_or_404(pk=pk)
    context = {"recipe_id": pk, "recipe": recipe}
    return render(request, "recipes/pages/detail.html", context)


def create(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Recipes",
        "recipes": [
            {"id": 1, "name": "Spaghetti Bolognese"},
            {"id": 2, "name": "Chicken Alfredo"},
            {"id": 3, "name": "Caesar Salad"},
        ],
    }
    return render(request, "recipes/pages/index.html", context)


def edit(request: HttpRequest, recipe_id: str) -> HttpResponse:
    return render(request, "recipes/edit.html", {"recipe_id": recipe_id})


def delete(request: HttpRequest, recipe_id: str) -> HttpResponse:
    return render(request, "recipes/delete.html", {"recipe_id": recipe_id})


def category(request: HttpRequest, pk: int) -> HttpResponse:
    recipes = get_list_or_404(
        Recipe,
        category__pk=pk,
        is_published=True,
    )
    context = {"title": "Recipes", "recipes": recipes}
    return render(request, "recipes/pages/category.html", context)
