from django.db import models


class RecipeCategory(models.Model):
    class Meta:
        verbose_name = "Recipe Category"
        verbose_name_plural = "Recipe Categories"

    name = models.CharField(max_length=255)
    description = models.TextField()


class Recipe(models.Model):
    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"

    title = models.CharField(max_length=255)
    description = models.TextField()
    preparation_time = models.PositiveIntegerField()
    cooking_time = models.PositiveIntegerField()
    servings = models.PositiveIntegerField()
    ingredients = models.TextField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, null=False, default="")
    categories = models.ManyToManyField(RecipeCategory)

    def __str__(self) -> str:
        return self.title
