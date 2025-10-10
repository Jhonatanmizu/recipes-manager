from django.test import TestCase
from django.urls import reverse

from recipes.models import Recipe, RecipeCategory


class RecipeURLsTestCase(TestCase):
    def setUp(self) -> None:
        self.category = RecipeCategory.objects.create(name="Test Category")
        self.recipe = Recipe.objects.create(
            title="Test Recipe",
            description="Simple description",
            is_published=True,
            preparation_time=10,
            servings=2,
            preparation_steps="Step 1: Test",
            preparation_steps_is_html=False,
            category=self.category,
        )

    def test_index_url_reverse_and_response(self):
        url = reverse("recipes:index")
        self.assertEqual(url, "/")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/pages/index.html")

    def test_category_url_reverse_and_response(self):
        url = reverse("recipes:category", kwargs={"pk": self.category.pk})
        expected_path = f"/recipes/category/{self.category.pk}/"
        self.assertEqual(url, expected_path)

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/pages/category.html")

    def test_detail_url_reverse_and_response(self):
        url = reverse("recipes:detail", kwargs={"pk": self.recipe.pk})
        expected_path = f"/detail/{self.recipe.pk}/"
        self.assertEqual(url, expected_path)

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/pages/detail.html")

    def test_category_url_returns_404_for_nonexistent_id(self):
        non_existent_id = self.category.pk + 999
        url = reverse("recipes:category", kwargs={"pk": non_existent_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_detail_url_returns_404_for_nonexistent_id(self):
        non_existent_id = self.recipe.pk + 999
        url = reverse("recipes:detail", kwargs={"pk": non_existent_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
