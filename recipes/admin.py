from django.contrib import admin

from .models import Recipe, RecipeCategory


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at")
    search_fields = ("title", "description")
    list_filter = ("created_at", "updated_at")
    ordering = ("-created_at",)
    date_hierarchy = "created_at"
    list_filter = ("created_at", "updated_at")


@admin.register(RecipeCategory)
class RecipeCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created_at",
    )
    search_fields = ("name",)
    ordering = ("-created_at",)
    date_hierarchy = "created_at"
