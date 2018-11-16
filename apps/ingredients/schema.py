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
    category = graphene.Field(
        CategoryType,
        id=graphene.Int(),
        name=graphene.String()
    )
    all_categories = graphene.List(CategoryType)

    ingredient = graphene.Field(
        IngredientType,
        id=graphene.Int(),
        name=graphene.String()
    )
    all_ingredients = graphene.List(IngredientType)

    def resolve_category(self, info, **kwargs):
        id = kwargs.get('id', None)
        name = kwargs.get('name', None)

        if id:
            return Category.objects.get(pk=id)
        if name:
            return Category.objects.get(name=name)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_ingredient(self, info, **kwargs):
        id = kwargs.get('id', None)
        name = kwargs.get('name', None)

        if id:
            return Ingredient.objects.get(pk=id)
        if name:
            return Ingredient.objects.get(name=name)

    def resolve_all_ingredients(self, info, **kwargs):
        return Ingredient.objects.select_related('category').all()

