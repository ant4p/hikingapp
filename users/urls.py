from django.urls import path

from users.views import ProfileUser, LoginUser, RegisterUser

app_name = 'users'

urlpatterns = [
    path('profile/', ProfileUser.as_view(), name='profile'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
]
