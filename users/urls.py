from django.contrib import admin
from django.urls import path, include
from users.views import signIn, logOut, dashboard, manager_dashboard, signUp, update, delete_user

urlpatterns = [
    path('dashboard/<int:id>/', dashboard, name='dashboard'),
    path('manager/', manager_dashboard, name='manager'),
    path('register/', signUp, name='signUp'),
     path('login/',signIn, name='signIn' ),
    path('logout/', logOut, name='logOut'), 
    path('update-user/<int:id>/', update, name='update-user'),
    path('delete-user/<int:id>/', delete_user, name='delete-user')
]
