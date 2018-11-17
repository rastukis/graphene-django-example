import graphene

from graphene_django.debug import DjangoDebug

from apps.ingredients.schema import QueryIngredients
from apps.posts.schema import QueryPost

class Query(QueryIngredients, graphene.ObjectType):

    debug = graphene.Field(DjangoDebug, name='__debug')
    pass

schema = graphene.Schema(query=Query)