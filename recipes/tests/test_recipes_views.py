from django.urls import resolve, reverse

from recipes import views as recipe_views
from recipes.models import Recipe
from recipes.tests.test_recipes_base import RecipeTestBase


class RecipeViewsTestCase(RecipeTestBase):
    # ========================
    # Index View Tests
    # ========================

    def test_index_view_resolves_to_correct_function(self) -> None:
        view = resolve(reverse("recipes:index"))
        self.assertIs(view.func, recipe_views.index)

    def test_index_view_returns_200_when_recipes_exist(self) -> None:
        response = self.client.get(reverse("recipes:index"))
        self.assertEqual(response.status_code, 200)

    def test_index_view_shows_message_when_no_recipes_exist(self) -> None:
        Recipe.objects.all().delete()
        response = self.client.get(reverse("recipes:index"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("No recipes found here.", response.content.decode("utf-8"))

    def test_index_has_correct_context(self) -> None:
        response = self.client.get(reverse("recipes:index"))
        self.assertIn("recipes", response.context)
        self.assertEqual(
            list(response.context["recipes"]),
            list(Recipe.objects.filter(is_published=True).order_by("-id")[:6]),
        )

    def test_index_shows_only_published_recipes(self) -> None:
        not_published_recipe = self.recipes[0]
        not_published_recipe.is_published = False
        not_published_recipe.save()
        response = self.client.get(reverse("recipes:index"))
        self.assertNotIn(
            Recipe.objects.filter(is_published=False).first(),
            response.context["recipes"],
        )

    # ========================
    # Category View Tests
    # ========================

    def test_category_view_resolves_to_correct_function(self) -> None:
        url = reverse("recipes:category", kwargs={"pk": self.category.pk})
        view = resolve(url)
        self.assertIs(view.func, recipe_views.category)

    def test_category_view_returns_200_when_category_exists(self) -> None:
        url = reverse("recipes:category", kwargs={"pk": self.category.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_category_view_returns_404_when_category_does_not_exist(self) -> None:
        non_existent_id = self.category.pk + 999
        url = reverse("recipes:category", kwargs={"pk": non_existent_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_category_view_has_correct_context(self) -> None:
        url = reverse("recipes:category", kwargs={"pk": self.category.pk})
        response = self.client.get(url)
        self.assertIn("recipes", response.context)
        self.assertEqual(
            list(response.context["recipes"]),
            list(
                Recipe.objects.filter(
                    category=self.category,
                    is_published=True,
                )
            ),
        )

    def test_category_view_shows_only_published_recipes(self) -> None:
        not_published_recipe = self.recipes[0]
        not_published_recipe.is_published = False
        not_published_recipe.save()
        url = reverse("recipes:category", kwargs={"pk": self.category.pk})
        response = self.client.get(url)
        self.assertNotIn(
            Recipe.objects.filter(is_published=False).first(),
            response.context["recipes"],
        )

    # ========================
    # Detail View Tests
    # ========================

    def test_detail_view_resolves_to_correct_function(self) -> None:
        recipe = self.recipes[0]
        url = reverse("recipes:detail", kwargs={"pk": recipe.pk})
        view = resolve(url)
        self.assertIs(view.func, recipe_views.detail)

    def test_detail_view_returns_200_when_recipe_exists(self) -> None:
        recipe = self.recipes[0]
        url = reverse("recipes:detail", kwargs={"pk": recipe.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_view_returns_404_when_recipe_does_not_exist(self) -> None:
        non_existent_id = max(r.pk for r in self.recipes) + 999
        url = reverse("recipes:detail", kwargs={"pk": non_existent_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_detail_view_shows_only_published_recipe(self) -> None:
        not_published_recipe = self.recipes[0]
        not_published_recipe.is_published = False
        not_published_recipe.save()
        url = reverse("recipes:detail", kwargs={"pk": not_published_recipe.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_detail_view_has_correct_context(self) -> None:
        recipe = self.recipes[0]
        url = reverse("recipes:detail", kwargs={"pk": recipe.pk})
        response = self.client.get(url)
        self.assertIn("recipe", response.context)
        self.assertEqual(response.context["recipe"], recipe)
