from rest_framework import serializers
from .models import UserProfile
from .models import Recipe

class UserProfileSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(required=True, write_only=True)

    class Meta:
        model = UserProfile
        fields= ('id', 'name', 'bio', 'image')

class RecipeSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(required=True, write_only=True)

    class Meta:
        model = Recipe
        fields = ('id', 'user_profile', 'title', 'image', 'instructions', 'equipment', 'ingredients')