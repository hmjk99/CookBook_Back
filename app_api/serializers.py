from rest_framework import serializers
from .models import UserProfile
from .models import Recipe
from .models import FavoriteRecipe

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields= ('id', 'username', 'bio', 'image')

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'user_profile', 'title', 'image', 'instructions', 'equipment', 'ingredients')

class FavoriteRecipeSerializers(serializers.ModelSerializer):

    class Meta:
        model = FavoriteRecipe
        fields = ('id', 'user', 'recipe')