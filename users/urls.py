from django.contrib.auth.views import LogoutView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, reverse_lazy

from users.views import ProfileUser, LoginUser, RegisterUser, PasswordChangeUser, PasswordChangeDoneUser, UserTrips

app_name = 'users'

urlpatterns = [
    path('trip/<str:username>', UserTrips.as_view(), name='user_trips'),

    path('profile/', ProfileUser.as_view(), name='profile'),
    path('register/', RegisterUser.as_view(), name='register'),

    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('password_change/', PasswordChangeUser.as_view(),
         name='password_change'),
    path('password_change/done/', PasswordChangeDoneUser.as_view(),
         name='password_change_done'),

    path('password_reset/',
         PasswordResetView.as_view(
             template_name='users/password_reset.html',
             email_template_name='users/password_reset_email.html',
             success_url=reverse_lazy('users:password_reset_done')
         ),
         name='password_reset'),
    path('password_reset_done/',
         PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),

    path('password_reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html",
            success_url=reverse_lazy("users:password_reset_complete")
         ),
         name='password_reset_confirm'),
    path('password_reset/complete/',
         PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),
         name='password_reset_complete'),

]
