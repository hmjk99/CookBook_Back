from django.urls import path
from . import views

urlpatterns = [
    path('api/recipes', views.RecipeList.as_view(), name='recipe_list'),
    path('api/recipes/<int:pk>', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('api/register', views.UserRegister.as_view(), name='register'),
	path('api/login', views.UserLogin.as_view(), name='login'),
	path('api/logout', views.UserLogout.as_view(), name='logout'),
	path('api/user', views.UserProfileList.as_view(), name='user'),
    path('api/user/<int:pk>', views.UserProfileDetail.as_view(), name='userprofile_detail'),
]

# {
#     "email":"test@example.com",
#     "password":"testing123"
# }

# test@test.com
# tester123