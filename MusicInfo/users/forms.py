from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (UserCreationForm, PasswordChangeForm,
                                       PasswordResetForm, SetPasswordForm)

User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class PasswordChangeForm(PasswordChangeForm):
    class Meta(PasswordChangeForm):
        model = User


class PasswordResetForm(PasswordResetForm):
    class Meta(PasswordResetForm):
        model = User


class PasswordSetForm(SetPasswordForm):
    class Meta(PasswordResetForm):
        model = User
