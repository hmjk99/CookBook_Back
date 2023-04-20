from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.exceptions import ValidationError
from .models import UserProfile
from .models import Recipe


UserModel = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = '__all__'
	def create(self, clean_data):
		user_obj = UserModel.objects.create_user(email=clean_data['email'], password=clean_data['password'])
		user_obj.username = clean_data['username']
		user_obj.save()
		return user_obj

# class UserLoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField()

#     def validate(self, data):
#         """
#         Check that the input data contains only `email` and `password` fields.
#         """
#         if set(data.keys()) != set(['email', 'password']):
#             raise serializers.ValidationError("Invalid fields.")
#         return data

#     def check_user(self, clean_data):
#         user = authenticate(username=clean_data['email'], password=clean_data['password'])
#         if not user:
#             raise ValidationError('user not found')
#         return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        """
        Check that the input data contains only `email` and `password` fields.
        """
        if set(data.keys()) != set(['email', 'password']):
            raise serializers.ValidationError("Invalid fields.")
        return data

    def validate_email(self, value):
        user = authenticate(username=value, password=self.initial_data['password'])
        if not user:
            raise serializers.ValidationError("Invalid email or password.")
        return value
	
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields= ('id', 'email', 'username', 'password', 'name', 'bio', 'image')

class RecipeSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(read_only=True)
    class Meta:
        model = Recipe
        fields = ('id', 'user_profile', 'title', 'image', 'instructions', 'equipment', 'ingredients')