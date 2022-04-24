from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.user_list),
    path('sessions/', views.session_list),
    path('user/<int:pk>/', views.user_detail),
    path('login/', views.login),
    path('logout/', views.logout),
    path('levels/', views.levels_list),
    path('songs/', views.levels_list),
    path('level/<int:pk>/', views.level_detail),
    path('attempts/', views.attempt_list),
    path('attempt/<int:pk>', views.levels_list),

]