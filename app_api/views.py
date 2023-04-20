from django.shortcuts import render
from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import UserProfileSerializer, UserRegisterSerializer, UserLoginSerializer, RecipeSerializer
from .models import UserProfile
from .models import Recipe
from rest_framework import permissions, status
from rest_framework.permissions import IsAdminUser
from .validations import custom_validation, validate_email, validate_password

# Create your views here.
class UserRegister(APIView):
	permission_classes = (permissions.AllowAny,)
	def post(self, request):
		clean_data = custom_validation(request.data)
		serializer = UserRegisterSerializer(data=clean_data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.create(clean_data)
			if user:
				user.name = clean_data.get('name')
				user.bio = clean_data.get('bio')
			if request.FILES.get('image'):
				user.image = request.FILES.get('image')
				user.save()
			if user:
				return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = (SessionAuthentication,)
	##
	def post(self, request):
		data = request.data
		assert validate_email(data)
		assert validate_password(data)
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.check_user(data)
			login(request, user)
			return Response(serializer.data, status=status.HTTP_200_OK)


class UserLogout(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = ()
	def post(self, request):
		logout(request)
		return Response(status=status.HTTP_200_OK)


class UserProfileList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, IsAdminUser)
	authentication_classes = (SessionAuthentication,)
	serializer_class = UserProfileSerializer

	def get_queryset(self):
		return UserProfile.objects.filter(pk=self.request.user.pk)

class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all().order_by('id')
    serializer_class = UserProfileSerializer

class RecipeList(generics.ListCreateAPIView):
	permission_classes = (permissions.AllowAny,)
	# authentication_classes = (SessionAuthentication,)
    
	queryset = Recipe.objects.all().order_by('id')
	serializer_class = RecipeSerializer

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.AllowAny,)
	# authentication_classes = (SessionAuthentication,)

	queryset = Recipe.objects.all().order_by('id')
	serializer_class = RecipeSerializer