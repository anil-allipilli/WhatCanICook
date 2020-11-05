from django.db import models


class Group(models.Model):
    group = models.CharField(max_length=16)

    def __str__(self):
        return self.group


class Ingredient(models.Model):

    name = models.CharField(max_length=128)
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Recipe(models.Model):

    title = models.CharField(max_length=128)
    ingredients = models.ManyToManyField(
        Ingredient)

    ingredients_list = models.TextField()
    preparation_steps = models.TextField()

    def __str__(self):
        return self.title
