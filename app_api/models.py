from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class UserProfile(models.Model):
    name = models.CharField(max_length=32, null=True)
    bio = models.CharField(max_length=128)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='recipes', null=True)
    title = models.CharField(max_length=32, null=True)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    imageUrl = models.CharField(null = True)
    instructions = models.TextField(null=True)
    equipment = models.CharField(max_length=255, null=True)
    ingredients = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title
