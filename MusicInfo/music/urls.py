from django.urls import path

from . import views
app_name = 'music'
namespace = 'music'
urlpatterns = [
    path('', views.index, name='index'),
    path('music/<int:music_id>/comment/', views.add_comment,
         name='add_comment'),
    path('music/<int:music_id>/edit/', views.edit_music, name='edit_music'),
    path('music/<int:music_id>/', views.music_detail, name='music_detail'),
    path('profile/<str:username>/', views.author_user, name='author_user'),
    path('authors/', views.get_authors, name='authors'),
    path('author/<int:id>/', views.author, name='author'),
    path('genres/', views.get_genres, name='genres'),
    path('genre/<int:id>/', views.genre, name='genre'),
    path('create/music/', views.create_music, name='create_music'),
    path('create/author/', views.create_author, name='create_author'),
    path('create/', views.create, name='create'),
]
