from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .utils import factory


def index(request: HttpRequest) -> HttpResponse:
    recipes = [factory.make_recipe() for _ in range(20)]
    context = {"title": "Recipes", "recipes": recipes}
    return render(request, "recipes/pages/index.html", context)


def detail(request: HttpRequest, pk: int) -> HttpResponse:
    recipe = factory.make_recipe()
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
