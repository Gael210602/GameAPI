from django.urls import path
from . import views


urlpatterns = [
    path('api/users/', views.user_list),
    path('api/sessions/', views.session_list),
    path('api/user/<int:pk>/', views.user_detail),
    path('api/login/', views.login),
    path('api/logout/', views.logout),
    path('api/levels/', views.levels_list),
    path('api/songs/', views.levels_list),
    path('api/level/<int:pk>/', views.level_detail),
    path('api/attempts/', views.attempt_list),
    path('api/attempt/<int:pk>/', views.levels_list),
    path('api/gameVariables/', views.variables_list),
    path('api/gameVariable/<int:pk>/', views.single_variables_user),

    path('api/grafica/', views.grafica),

]