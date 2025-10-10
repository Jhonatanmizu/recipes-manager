from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views as recipe_views
from recipes.models import Recipe, RecipeCategory


class RecipeViewsTestCase(TestCase):
    def setUp(self) -> None:
        self.category = RecipeCategory.objects.create(name="Main Category")
        self.recipes = self._create_recipes(self.category)

    def _create_recipes(self, category) -> list[Recipe]:
        recipes = [
            Recipe.objects.create(
                title=f"Recipe {i}",
                description="Delicious recipe",
                is_published=True,
                preparation_time=30,
                servings=4,
                preparation_steps="Step 1: Do this. Step 2: Do that.",
                preparation_steps_is_html=False,
                category=category,
            )
            for i in range(1, 6)
        ]
        return recipes

    # ========================
    # Index View Tests
    # ========================

    def test_index_view_resolves_to_correct_function(self):
        view = resolve(reverse("recipes:index"))
        self.assertIs(view.func, recipe_views.index)

    def test_index_view_returns_200_when_recipes_exist(self):
        response = self.client.get(reverse("recipes:index"))
        self.assertEqual(response.status_code, 200)

    def test_index_view_shows_message_when_no_recipes_exist(self):
        Recipe.objects.all().delete()
        response = self.client.get(reverse("recipes:index"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("No recipes found here.", response.content.decode("utf-8"))

    # ========================
    # Category View Tests
    # ========================

    def test_category_view_resolves_to_correct_function(self):
        url = reverse("recipes:category", kwargs={"pk": self.category.pk})
        view = resolve(url)
        self.assertIs(view.func, recipe_views.category)

    def test_category_view_returns_200_when_category_exists(self):
        url = reverse("recipes:category", kwargs={"pk": self.category.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_category_view_returns_404_when_category_does_not_exist(self):
        non_existent_id = self.category.pk + 999
        url = reverse("recipes:category", kwargs={"pk": non_existent_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    # ========================
    # Detail View Tests
    # ========================

    def test_detail_view_resolves_to_correct_function(self):
        recipe = self.recipes[0]
        url = reverse("recipes:detail", kwargs={"pk": recipe.pk})
        view = resolve(url)
        self.assertIs(view.func, recipe_views.detail)

    def test_detail_view_returns_200_when_recipe_exists(self):
        recipe = self.recipes[0]
        url = reverse("recipes:detail", kwargs={"pk": recipe.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_view_returns_404_when_recipe_does_not_exist(self):
        non_existent_id = max(r.pk for r in self.recipes) + 999
        url = reverse("recipes:detail", kwargs={"pk": non_existent_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
