from django.urls import path
from .views.users_view import *
from .views.teams_view import *
from .views.app_view import *
from .views.api_view import *

urlpatterns = [
    # App
    path('home/', AppHome.as_view(), name='app_home'),

    # Users 
    path('users/list/',  UsersList.as_view(), name='users_list'),
    path('users/create/', UsersCreate.as_view(), name='users_create'),
    path('users/delete/<int:id>/', UsersDelete.as_view(), name='users_delete'),
    path('users/update/<int:id>/', UsersUpdate.as_view(), name='users_update'),
    path('users/shuffle/', UsersShuffle.as_view(), name='users_shuffle'),
    path('users/reset/', UsersReset.as_view(), name='users_reset'),

    # Teams
    path('teams/list/', TeamsList.as_view(), name='teams_list'),
    path('teams/create/', TeamsCreate.as_view(), name='teams_create'),
    path('teams/delete/<int:id>/', TeamsDelete.as_view(), name='teams_delete'),
    path('teams/update/<int:id>/', TeamsUpdate.as_view(), name='teams_update'),

    # Api
    path('api/users/list/', ApiUsersList.as_view(), name='api_users_list'),
    path('api/users/create/', ApiUsersCreate.as_view(), name='api_users_create'),
    path('api/users/delete/<int:id>/', APIUsersDelete.as_view(), name='api_users_delete'),
    path('api/users/update/<int:id>/', APIUsersUpdate.as_view(), name='api_users_update'),
    path('api/users/shuffle/', APIUsersShuffle.as_view(), name='api_users_shuffle'),
    path('api/users/reset/', APIUsersReset.as_view(), name='api_users_reset'),
]
