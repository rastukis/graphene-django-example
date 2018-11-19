from graphene import relay, ObjectType, Node

from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.rest_framework.mutation import SerializerMutation

# Modelos
from apps.ingredients.models import Category, Ingredient

# Serializer
from apps.ingredients.serializers import IngredientSerializer

class CategoryNode(DjangoObjectType):

    class Meta:
        model = Category
        filter_fields = ['name', 'ingredients']
        interfaces = (Node, )

class IngredientNode(DjangoObjectType):

    class Meta:
        model = Ingredient
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'notes': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        interfaces = (relay.Node, )

class IngredientMutation(SerializerMutation):

    class Meta:
        serializer_class = IngredientSerializer
        model_operations = ['create', 'update']
        lookup_field = 'id'

class QueryIngredients(object):
    category = Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    ingredient = Node.Field(IngredientNode)
    all_ingredients = DjangoFilterConnectionField(IngredientNode)

"""
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
"""
