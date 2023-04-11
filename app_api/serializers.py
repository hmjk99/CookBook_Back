from rest_framework import serializers
from .models import UserProfile
from .models import Recipe

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields= ('id', 'user', 'bio', 'img')

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'instructions', 'equipments', 'ingredients', 'recipes_id')