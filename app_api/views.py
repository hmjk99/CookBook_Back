from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
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

def update_image(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    serializer = RecipeSerializer(recipe, data=request.data)
    if serializer.is_valid():
        if 'image' in request.data:
            recipe.image.delete()
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)