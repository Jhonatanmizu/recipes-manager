from recipes.models import Recipe


class RecipeService:
    def get_recipe(self, pk: int) -> Recipe | None:
        return Recipe.objects.filter(pk=pk).first()

    def get_published_recipes(self) -> list[Recipe]:
        return list(Recipe.objects.filter(is_published=True).order_by("-created_at"))

    def create_recipe(self, recipe_data: Recipe) -> Recipe:
        new_recipe = Recipe(recipe_data)
        new_recipe.save()
        return new_recipe

    def update_recipe(self, pk: int, recipe_data: dict) -> Recipe | None:
        recipe = self.get_recipe(pk)
        if recipe:
            for key, value in recipe_data.items():
                setattr(recipe, key, value)
            recipe.save()
            return recipe
        return None

    def delete_recipe(self, pk: int) -> bool:
        recipe = self.get_recipe(pk)
        if recipe:
            recipe.delete()
            return True
        return False

    def toggle_publish_status(self, pk: int) -> Recipe | None:
        recipe = self.get_recipe(pk)
        if recipe:
            recipe.is_published = not recipe.is_published
            recipe.save()
            return recipe
        return None
