from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views as recipes_views


class RecipeViewsTestCase(TestCase):
    def test_recipe_index_view_function_is_correct(self):
        view = resolve(reverse("recipes:index"))
        self.assertIs(view.func, recipes_views.index)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse("recipes:category", kwargs={"pk": 1}))
        self.assertIs(view.func, recipes_views.category)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse("recipes:detail", kwargs={"pk": 1}))
        self.assertIs(view.func, recipes_views.detail)
