from django.db import models
from django.db.models import Count


class Group(models.Model):
    group = models.CharField(max_length=16)

    def __str__(self):
        return self.group


class Ingredient(models.Model):

    name = models.CharField(max_length=128)
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class RecipeManager(models.Manager):
    def get_recipes(self, query_string, min_num_of_ingredients):
        ingredients_ids = query_string.split("-")
        # Least number of Ingredients
        if(min_num_of_ingredients == ""):
            min_num_of_ingredients = 3
        n = min_num_of_ingredients
        # Select Ingredients which are main i.e of group ids 1, 3, 4, 6, 7
        ingredients = Ingredient.objects.filter(
            id__in=ingredients_ids).filter(group=4)
        if(ingredients.count() > 0):
            queryset = Recipe.objects.annotate(ing_count=Count('ingredients')).filter(
                ingredients__in=ingredients).exclude(ing_count__lt=n).order_by("ing_count")
            if(queryset.count() > 0):
                return queryset
        ingredients = Ingredient.objects.filter(
            id__in=ingredients_ids).filter(group=7)
        if(ingredients.count() > 0):
            queryset = Recipe.objects.annotate(ing_count=Count('ingredients')).filter(
                ingredients__in=ingredients).exclude(ing_count__lt=n).order_by("ing_count")
            if(queryset.count() > 0):
                return queryset
        ingredients = Ingredient.objects.filter(
            id__in=ingredients_ids).filter(group=3)
        if(ingredients.count() > 0):
            queryset = Recipe.objects.annotate(ing_count=Count('ingredients')).filter(
                ingredients__in=ingredients).exclude(ing_count__lt=n).order_by("ing_count")
            if(queryset.count() > 0):
                return queryset
        ingredients = Ingredient.objects.filter(
            id__in=ingredients_ids).filter(group=1)
        if(ingredients.count() > 0):
            queryset = Recipe.objects.annotate(ing_count=Count('ingredients')).filter(
                ingredients__in=ingredients).exclude(ing_count__lt=n).order_by("ing_count")
            if(queryset.count() > 0):
                return queryset
        ingredients = Ingredient.objects.filter(
            id__in=ingredients_ids).exclude(group__in=[2, 5, 8, 9, 10])
        if(ingredients.count() > 0):
            queryset = Recipe.objects.annotate(ing_count=Count('ingredients')).filter(
                ingredients__in=ingredients).exclude(ing_count__lt=n).order_by("ing_count")
            return queryset
        ingredients = Ingredient.objects.filter(
            id__in=ingredients_ids)
        return Recipe.objects.annotate(ing_count=Count('ingredients')).filter(
            ingredients__in=ingredients).exclude(ing_count__lt=n).order_by("ing_count")


class Recipe(models.Model):

    title = models.CharField(max_length=128)
    ingredients = models.ManyToManyField(
        Ingredient)
    ingredients_list = models.TextField()
    preparation_steps = models.TextField()

    objects = RecipeManager()

    def __str__(self):
        return self.title
