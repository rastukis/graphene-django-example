import graphene

from apps.ingredients.schema import QueryIngredients

class Query(QueryIngredients, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)