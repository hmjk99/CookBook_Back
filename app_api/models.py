from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class UserProfile(AbstractUser):
    username = models.CharField(max_length=150, unique=True, default='default_username')
    bio = models.CharField(max_length=128)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='user_profiles'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='user_profiles'
    )


    def __str__(self):
        return self.username


class Recipe(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='recipes', null=True)
    title = models.CharField(max_length=32, null=True)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    imageUrl = models.CharField(null=True)
    instructions = models.TextField(null=True)
    equipment = models.CharField(max_length=255, null=True)
    ingredients = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title

class FavoriteRecipe(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='favorite_recipes')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='favorited_by')

    def __str__(self):
        return f"{self.user.username}'s favorite recipe: {self.recipe.title}"