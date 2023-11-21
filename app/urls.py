from django.urls import path
from .views.users_view import *
from .views.app_view import *

urlpatterns = [
    # app
    path('home/', AppHome.as_view(), name='app_home'),

    # users 
    path('users/list/',  UsersList.as_view(), name='users_list'),
    path('users/create/', UsersCreate.as_view(), name='users_create'),
    path('users/delete/<int:id>/', UsersDelete.as_view(), name='users_delete'),
    path('users/update/<int:id>/', UsersUpdate.as_view(), name='users_update')
]
