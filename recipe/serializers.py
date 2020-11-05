from rest_framework import serializers

from recipe.models import Ingredient, Group, Recipe


class IngredientSerializers(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'group']
        read_only_fields = fields


class GroupSerializers(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ['id', 'group']
        read_only_fields = fields


class RecipeListSerializers(serializers.ModelSerializer):

    ingredients = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'ingredients']
        read_only_fields = fields


class RecipeDetailSerializers(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'ingredients_list', 'preparation_steps']
        read_only_fields = fields
