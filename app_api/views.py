from django.shortcuts import render
from rest_framework import generics
from .serializers import UserProfileSerializer
from .serializers import RecipeSerializer
from .models import UserProfile
from .models import Recipe

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

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all().order_by('id')
    serializer_class = RecipeSerializer