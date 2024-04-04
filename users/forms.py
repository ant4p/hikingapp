from django import forms
from django.contrib.auth import get_user_model


class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = [
            'avatar',
            'username',
            'gender',
            'email',
            'birthday',
            'first_name',
            'last_name',

        ]

