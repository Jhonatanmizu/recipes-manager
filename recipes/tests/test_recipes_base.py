from django.contrib.auth.models import User
from django.test import TestCase

from recipes.models import Recipe, RecipeCategory


class RecipeTestBase(TestCase):
    def setUp(self) -> None:
        self.author = self.create_authors(data=None)
        self.category = self.create_category(name="Category 1")
        self.recipes = self.create_recipes()
        return super().setUp()

    def create_authors(self, data: dict | None) -> User | None:
        if data:
            author = User.objects.create_user(
                username=data.get("username", "testuser"),
                email=data.get("email", "testuser@gmail.com"),
                password=data.get("password", "testpassword123"),
            )
            return author
        author = User.objects.create_user(
            username="testuser",
            email="testuser@gmail.com",
            password="testpassword123",
        )
        return author

    def create_category(self, name: str) -> RecipeCategory:
        return RecipeCategory.objects.create(name=name)

    def create_recipes(
        self,
    ) -> list[Recipe]:
        instances = [
            Recipe(
                title=f"Recipe {i}",
                description="Delicious recipe",
                slug=f"recipe-{i}",
                is_published=True,
                preparation_time_unit="Minutes",
                preparation_time=30,
                servings_unit="People",
                servings=4,
                preparation_steps="Step 1: Do this. Step 2: Do that.",
                preparation_steps_is_html=False,
                category=self.category,
                author=self.author,
            )
            for i in range(1, 6)
        ]
        Recipe.objects.bulk_create(instances)
        return list(Recipe.objects.order_by("title"))
