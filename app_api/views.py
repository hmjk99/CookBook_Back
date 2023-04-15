from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from .serializers import UserProfileSerializer
from .serializers import RecipeSerializer
from .models import UserProfile
from .models import Recipe
from .models import FavoriteRecipe

# Create your views here.
class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all().order_by('id')
    serializer_class = UserProfileSerializer

class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all().order_by('id')
    serializer_class = UserProfileSerializer

class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all().order_by('id')
    serializer_class = RecipeSerializer

    def perform_create(self, serializer):
        user_profile = self.request.user.userprofile
        serializer.save(user_profile=user_profile)

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all().order_by('id')
    serializer_class = RecipeSerializer


class AddToFavorite(APIView):
    def post(self, request, recipe_id):
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        user_profile = request.user.userprofile
        favorite_recipe = FavoriteRecipe.objects.create(user=user_profile, recipe=recipe)
        return Response({'message': 'Recipe added to favorites.'}, status=status.HTTP_201_CREATED)
    
class FavoriteRecipeList(APIView):
    def get(self, request):
        user_profile = request.user.userprofile
        favorite_recipes = FavoriteRecipe.objects.filter(user=user_profile)
        serializer = RecipeSerializer(favorite_recipes, many=True)
        return Response(serializer.data)

    

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'User logged in succesfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)