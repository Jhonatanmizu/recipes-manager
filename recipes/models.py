from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class RecipeCategory(models.Model):
    class Meta:
        verbose_name = "Recipe Category"
        verbose_name_plural = "Recipe Categories"

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Recipe(models.Model):
    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"

    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True,unique=True)
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField(blank=True, null=True)
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to="recipes/covers/%Y/%m/%d/", blank=True, null=True)
    category = models.ForeignKey(RecipeCategory, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
