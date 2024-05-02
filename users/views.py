from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, ListView

from trip.models import Trip
from users.forms import ProfileUserForm, LoginUserForm, RegisterUserForm, PasswordChangeUserForm


class UserTrips(ListView):
    template_name = 'trip/index.html'
    context_object_name = 'trips'
    paginate_by = 3

    def get_queryset(self):
        return (Trip.objects.filter(user__username=self.kwargs['username'], published=True).
                select_related('category').
                prefetch_related('user', 'tag'))


class ProfileUser(UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    context_object_name = 'user'

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

    # def get_success_url(self):
    #     return reverse_lazy('home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class PasswordChangeUser(PasswordChangeView):
    form_class = PasswordChangeUserForm
    success_url = reverse_lazy('users:password_change_done')
    template_name = 'users/password_change.html'


class PasswordChangeDoneUser(PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'
