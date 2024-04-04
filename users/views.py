from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from users.forms import ProfileUserForm


# Create your views here.
class ProfileUser(UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    context_object_name = 'user'

    def get_success_url(self):
        return reverse_lazy('users: profile')

    def get_object(self, queryset=None):
        return self.request.user
