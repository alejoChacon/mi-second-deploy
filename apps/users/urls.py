from django.urls import path
from .system_logueo import SignUp,UserList

urlpatterns = [
    path('sign-up/',SignUp.as_view(),name='signUp'),
    path('',UserList.as_view(),name='userList'),
]