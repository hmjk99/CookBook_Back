from django.urls import path
from . import views

urlpatterns = [
    path('api/userprofiles', views.UserProfileList.as_view(), name='userprofile_list'),
    path('api/userprofiles/<int:pk>', views.UserProfileDetail.as_view(), name='userprofile_detail'),
    path('api/recipes', views.RecipeList.as_view(), name='recipe_list'),
    path('api/recipes/<int:pk>', views.RecipeDetail.as_view(), name='recipe_detail'),
]