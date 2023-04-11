from django.contrib import admin

# Register your models here.
from .models import UserProfile
admin.site.register(UserProfile)
from .models import Recipe
admin.site.register(Recipe)