from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .forms import MusicForm, AuthorForm, CommentForm
from .models import Music, Genre, Author, User
from .utils import pages
music_numb = 4


def index(request):
    title = 'Последние обновления на сайте'
    music_list = Music.objects.all()
    page_obj = pages(request, music_list, music_numb)
    context = {
        'title': title,
        'page_obj': page_obj,
    }
    return render(request, 'music/index.html', context)


def music_detail(request, music_id):
    music = get_object_or_404(Music, id=music_id)
    title = music
    comments = music.comments.all()
    form = CommentForm(request.POST or None, files=request.FILES or None)
    context = {
        'music': music,
        'title': title,
        'comments': comments,
        'form': form,
    }
    return render(request, 'music/music_detail.html', context)


def get_genres(request):
    title = 'Жанры песен'
    genres = Genre.objects.all()
    context = {
        'title': title,
        'genres': genres,
    }
    return render(request, 'music/genres.html', context)


def genre(request, id):
    genre = get_object_or_404(Genre, id=id)
    context = profile(request, genre)
    return render(request, 'music/genre.html', context)


def get_authors(request):
    title = 'Авторы'
    authors = Author.objects.all()
    context = {
        'title': title,
        'authors': authors,
    }
    return render(request, 'music/authors.html', context)


def author(request, id):
    author = get_object_or_404(Author, id=id)
    context = profile(request, author)
    return render(request, 'music/author.html', context)


def author_user(request, username):
    author = get_object_or_404(User, username=username)
    context = profile(request, author)
    return render(request, 'music/author.html', context)


def profile(request, profile):
    music_list = profile.music.all()
    page_obj = pages(request, music_list, music_numb)
    context = {
        'author': profile,
        'page_obj': page_obj,
        'genre': profile}
    return context


def create(request):
    title = 'Добавить контент'
    context = {'title': title}
    return render(request, 'music/create.html', context)


@login_required
def create_music(request):
    title = 'Новая песня'
    music_info = 'Добавить песню '
    form = MusicForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        form.save(commit=False).author_user_id = request.user.pk
        form.save()
        return redirect('music:index')
    context = {
        'title': title,
        'music_info': music_info,
        'form': form,
    }
    return render(request, 'music/create_music.html', context)


@login_required
def edit_music(request, music_id):
    music = get_object_or_404(Music, id=music_id)
    user = request.user.get_username()
    is_edit = True
    title = 'Редактировать песню'
    music_info = 'Редактировать запись'
    if user != music.author_user.username:
        return redirect('music:music_detail', music.id)
    form = MusicForm(
        request.POST or None,
        files=request.FILES or None,
        instance=music)
    if form.is_valid():
        form.save()
        return redirect('music:music_detail', music.id)
    context = {
        'form': form,
        'music': music,
        'is_edit': is_edit,
        'title': title,
        'music_info': music_info
    }
    return render(request, 'music/create_music.html', context)


@login_required
def create_author(request):
    title = 'Новый автор'
    music_info = 'Добавить автора'
    form = AuthorForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        form.save(commit=False).author_user_id = request.user.pk
        form.save()
        return redirect('music:index')
    context = {
        'title': title,
        'music_info': music_info,
        'form': form,
    }
    return render(request, 'music/create_author.html', context)


@login_required
def add_comment(request, music_id):
    music = get_object_or_404(Music, id=music_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author_user = request.user
        comment.music = music
        comment.save()
    return redirect('music:music_detail', music_id=music_id)
