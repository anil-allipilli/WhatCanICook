from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action

from recipe.serializers import IngredientSerializers, GroupSerializers, RecipeListSerializers, RecipeDetailSerializers
from recipe.models import Ingredient, Group, Recipe


class RecipeViewPagination(PageNumberPagination):
    page_size = 500
    page_size_query_param = 'page_size'


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all().order_by('name')
    serializer_class = IngredientSerializers


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('id')
    serializer_class = GroupSerializers


class RecipeViewSet(viewsets.ModelViewSet):
    pagination_class = RecipeViewPagination

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return RecipeDetailSerializers
        return RecipeListSerializers
