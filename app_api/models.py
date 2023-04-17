from django.db import models
from .managers import AppUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

	
class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=50, unique=True, default='youremail@example.com')
    username = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=32, null=True)
    bio = models.TextField(null=True)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = AppUserManager()
    def __str__(self):
	    return self.email



class Recipe(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='recipes', null=True)
    title = models.CharField(max_length=32, null=True)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    instructions = models.TextField(null=True)
    equipment = models.TextField(null=True)
    ingredients = models.TextField(null=True)

    def __str__(self):
        return self.title

class FavoriteRecipe(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='favorite_recipes')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='favorited_by')

    def __str__(self):
        return f"{self.user.username}'s favorite recipe: {self.recipe.title}"