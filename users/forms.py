import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm


class ProfileUserForm(forms.ModelForm):
    year = datetime.date.today().year
    birthday = forms.DateField(widget=forms.SelectDateWidget(years=tuple(range(year - 100, year - 5))))

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


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'password',
        ]


class RegisterUserForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('This email already used')
        return email


class PasswordChangeUserForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old password',
                                   widget=forms.PasswordInput())
    new_password1 = forms.CharField(label='New password',
                                    widget=forms.PasswordInput())
    new_password2 = forms.CharField(label='Repeat new password',
                                    widget=forms.PasswordInput())

