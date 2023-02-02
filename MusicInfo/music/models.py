from django.db import models
from django.contrib.auth import get_user_model
from embed_video.fields import EmbedVideoField

User = get_user_model()

GENRE_CHOICES = (
    ("RO", "Рок"),
    ("E", "Электроника"),
    ("P", "Поп"),
    ("C", "Классика"),
    ("F", "Фолк"),
    ("CO", "Кантри"),
    ("B", "Блюз"),
    ("F", "Фолк"),
    ("SH", "Шансон"),
    ("H", "Хип-поп"),
    ("RA", "Регги"),
    ("D", "Диско"),
    ("O", "Другое"),
)


class Author(models.Model):
    name = models.TextField()

    def __str__(self) -> str:
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=2, choices=GENRE_CHOICES, default="О")

    def __str__(self) -> str:
        return self.get_name_display()


class Music(models.Model):
    name = models.TextField(verbose_name="название песни",)
    text = models.TextField(verbose_name="текст песни",
                            help_text='Введите текст песни')
    translation = models.TextField(verbose_name="перевод песни",
                                   help_text='Если песня не на русском языке',
                                   blank=True)
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name="дата публикации")
    author_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='music',
        verbose_name="пользавотель")
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='music',
        verbose_name="автор песни")
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        related_name='music',
        verbose_name="жанр песни")
    video = EmbedVideoField(
        blank=True,
        verbose_name="видео",
        help_text='Ссылка на видео. Желательно Youtube.\
        Не все видео могут отображаться на сайте, из-за авторских прав')
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['-pub_date']


class Comment(models.Model):
    music = models.ForeignKey(Music,
                              on_delete=models.CASCADE,
                              related_name='comments')
    author_user = models.ForeignKey(User,
                                    on_delete=models.CASCADE,
                                    related_name='comments',
                                    verbose_name="Автор")
    text = models.TextField(verbose_name="текст комментария",
                            help_text='Введите текст комментария')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name="дата создания")

    def __str__(self) -> str:
        return self.text

    class Meta:
        ordering = ['-created']
