from django.db.models import Q
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Recipe


def get_recipe_or_404(pk: int) -> Recipe:
    recipe = get_object_or_404(Recipe, pk=pk, is_published=True)
    return recipe


def index(request: HttpRequest) -> HttpResponse:
    recipes = Recipe.objects.filter(is_published=True).order_by("-created_at")
    context = {"title": "Recipes", "recipes": recipes}
    return render(request, "recipes/pages/index.html", context)


def detail(request: HttpRequest, pk: int) -> HttpResponse:
    recipe = get_recipe_or_404(pk=pk)
    context = {"recipe_id": pk, "recipe": recipe}
    return render(request, "recipes/pages/detail.html", context)


def category(request: HttpRequest, pk: int) -> HttpResponse:
    recipes = get_list_or_404(
        Recipe,
        category__pk=pk,
        is_published=True,
    )
    context = {"title": "Recipes", "recipes": recipes}
    return render(request, "recipes/pages/category.html", context)


def search(request: HttpRequest) -> HttpResponse:
    search_term = request.GET.get("q", "").strip()
    if not search_term:
        raise Http404()
    recipes = Recipe.objects.filter(
        Q(Q(title__icontains=search_term) | Q(description__icontains=search_term)),
        is_published=True,
    ).order_by("-created_at")
    context = {
        "recipes": recipes,
        "search_term": search_term,
        "title": f"Search for {search_term} |",
    }
    return render(request, "recipes/pages/search.html", context)
