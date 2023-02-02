from django.forms import ModelForm
from django import forms
from .models import Music, Author, Comment


class MusicForm(ModelForm):
    class Meta:
        model = Music
        fields = ('name', 'text', 'translation', 'author', 'genre', 'video')

    def clean_text(self):
        return validate_text(self.cleaned_data['text'])


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ('name',)

    def clean_text(self):
        return validate_text(self.cleaned_data['text'])


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

    def clean_text(self):
        return validate_text(self.cleaned_data['text'])


def validate_text(data):
    if data.isspace():
        raise forms.ValidationError('Текстовое поле не может быть пустым!')
    return data
