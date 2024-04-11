from django.contrib.auth import views
from django.contrib.auth.views import LogoutView, PasswordChangeDoneView
from django.urls import path

from users.views import ProfileUser, LoginUser, RegisterUser, PasswordChangeUser, PasswordChangeDoneUser

app_name = 'users'

urlpatterns = [
    path('profile/', ProfileUser.as_view(), name='profile'),
    path('register/', RegisterUser.as_view(), name='register'),

    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('password_change/', PasswordChangeUser.as_view(),
         name='password_change'),
    path('password_change/done/', PasswordChangeDoneUser.as_view(),
         name='password_change_done'),


]
