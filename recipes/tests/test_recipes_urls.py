from django.test import TestCase
from django.urls import reverse


class RecipeURLsTestCase(TestCase):
    def test_recipe_url_is_correct(self):
        home_url = reverse("recipes:index")
        self.assertEqual(home_url, "/")
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/pages/index.html")

    def test_recipe_category_url_is_correct(self):
        category_url = reverse("recipes:category", kwargs={"pk": 1})
        self.assertEqual(category_url, "/recipes/category/1/")
        response = self.client.get("/recipes/category/1/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipes/pages/category.html")

    def test_recipe_detail_url_is_correct(self):
        detail_url = reverse("recipes:detail", kwargs={"pk": 2})
        self.assertEqual(detail_url, "/detail/2/")

    def test_404_recipe_category_url(self):
        response = self.client.get("recipes/category/99999/")
        self.assertEqual(response.status_code, 404)
