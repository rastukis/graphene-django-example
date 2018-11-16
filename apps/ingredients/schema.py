import graphene

from graphene_django import DjangoObjectType

from apps.ingredients.models import Category, Ingredient

class CategoryType(DjangoObjectType):

    class Meta:
        model = Category

class IngredientType(DjangoObjectType):

    class Meta:
        model = Ingredient

class QueryIngredients(object):
    all_categories = graphene.List(CategoryType)
    all_ingredients = graphene.List(IngredientType)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_ingredients(self, info, **kwargs):
        return Ingredient.objects.select_related('category').all()