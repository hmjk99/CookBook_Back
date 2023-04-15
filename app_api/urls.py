from django.urls import path
from . import views
from .views import FavoriteRecipeList, AddToFavorite, LoginView


urlpatterns = [
    path('api/userprofiles', views.UserProfileList.as_view(), name='userprofile_list'),
    path('api/userprofiles/<int:pk>', views.UserProfileDetail.as_view(), name='userprofile_detail'),
    path('api/recipes', views.RecipeList.as_view(), name='recipe_list'),
    path('api/recipes/<int:pk>', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('api/recipes/<int:recipe_id>/add-to-favorite/', AddToFavorite.as_view(), name='add-to-favorite'),
    path('api/favorite-recipes/', FavoriteRecipeList.as_view(), name='favorite-recipe-list'),
    path('api/login/', LoginView.as_view(), name='login')
]