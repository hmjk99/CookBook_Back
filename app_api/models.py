from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=128)
    image = models.ImageField()


class Recipe(models.Model):
    instructions: models.TextField()
    equipment: models.CharField(255)
    ingredients: models.CharField(255)
    # linking recipes to user models
    recipes_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    