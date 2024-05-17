import datetime
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.utils.translation import gettext_lazy as _


class ProfileUserForm(forms.ModelForm):
    year = datetime.date.today().year
    birthday = forms.DateTimeField(label=_('birthday'),
                                   widget=forms.SelectDateWidget(years=tuple(range(year - 100, year - 5))))

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'birthday',
            'gender',
            'avatar',

        ]


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = [
            _('username'),
            _('password'),
        ]


class RegisterUserForm(UserCreationForm):
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput())
    password2 = forms.CharField(label=_('Repeat password'), widget=forms.PasswordInput())

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
    old_password = forms.CharField(label=_('Old password'),
                                   widget=forms.PasswordInput())
    new_password1 = forms.CharField(label=_('New password'),
                                    widget=forms.PasswordInput())
    new_password2 = forms.CharField(label=_('Repeat new password'),
                                    widget=forms.PasswordInput())

