from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import (CreationForm, PasswordChangeForm, PasswordResetForm,
                    PasswordSetForm)


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('music:index')
    template_name = 'users/signup.html'


class PasswordChangeView(CreateView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('users:password_change_done')
    template_name = 'users/password_change_form.html'


class PasswordChangeDoneView(CreateView):
    template_name = 'users/password_change_done.html'


class PasswordResetView(CreateView):
    form_class = PasswordResetForm
    success_url = reverse_lazy('users:password_reset_done')
    template_name = 'users/password_reset_form.html'


class PasswordResetDoneView(CreateView):
    template_name = 'users/password_reset_done.html'


class PasswordResetConfirmView(CreateView):
    form_class = PasswordSetForm
    success_url = reverse_lazy('users:password_reset_complete')
    template_name = 'users/password_reset_confirm.html'


class PasswordResetCompleteView(CreateView):
    template_name = 'users/password_reset_complete.html'
