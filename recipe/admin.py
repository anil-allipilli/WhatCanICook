from django.contrib import admin
from recipe.models import Ingredient, Recipe, Group

admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Group)
