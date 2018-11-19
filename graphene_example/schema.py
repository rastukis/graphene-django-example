import graphene

from graphene_django.debug import DjangoDebug

from apps.ingredients.schema import QueryIngredients
from apps.posts.schema import QueryPost
from apps.ingredients.schema import IngredientMutation

class Query(QueryIngredients, graphene.ObjectType):

    debug = graphene.Field(DjangoDebug, name='__debug')
    pass

schema = graphene.Schema(query=Query, mutation=IngredientMutation)