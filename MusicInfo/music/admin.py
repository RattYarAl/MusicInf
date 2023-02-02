from django.contrib import admin
from .models import Author, Music, Genre, Comment


class MusicAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'name', 'text',
                    'pub_date', 'author_user', 'genre')
    list_filter = ('pub_date', 'author_user')
    empty_value_display = '-пусто-'


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'created', 'author_user',)
    search_fields = ('text',)
    list_filter = ('created',)
    empty_value_display = '-пусто-'


admin.site.register(Music, MusicAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Comment, CommentAdmin)
