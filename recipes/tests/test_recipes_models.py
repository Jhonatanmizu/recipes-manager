from recipes.models import Recipe
from recipes.tests.test_recipes_base import RecipeTestBase


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        return super().setUp()

    def test_recipe_str_representation(self) -> None:
        recipe = self.recipes[0]
        self.assertEqual(str(recipe), recipe.title)

    def test_recipe_is_published_default_value(self) -> None:
        recipe = Recipe(
            title="Unpublished Recipe",
            description="This recipe is not published yet.",
            slug="unpublished-recipe",
            preparation_time_unit="Minutes",
            preparation_time=20,
            servings_unit="People",
            servings=2,
            preparation_steps="Step 1: Do something.",
            preparation_steps_is_html=False,
            category=self.category,
            author=self.author,
        )
        recipe.save()
        self.assertFalse(recipe.is_published)

    def test_delete_recipe(self) -> None:
        recipe = self.recipes[0]
        recipe_pk = recipe.pk
        recipe.delete()
        self.assertTrue(recipe.is_deleted)
        self.assertIsNotNone(recipe.deleted_at)
        with self.assertRaises(Recipe.DoesNotExist):
            Recipe.objects.get(pk=recipe_pk)

    def test_restore_recipe(self) -> None:
        recipe = self.recipes[1]
        recipe.delete()
        deleted_recipe = Recipe.objects.filter(pk=recipe.pk).first()
        self.assertIsNone(deleted_recipe)

        recipe.restore()

        restored_recipe = Recipe.objects.filter(pk=recipe.pk).first()
        self.assertFalse(recipe.is_deleted)
        self.assertIsNone(recipe.deleted_at)
        self.assertIsNotNone(restored_recipe)
