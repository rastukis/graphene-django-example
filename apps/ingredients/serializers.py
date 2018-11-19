from rest_framework import serializers

from apps.ingredients.models import Ingredient

class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('name', 'notes')