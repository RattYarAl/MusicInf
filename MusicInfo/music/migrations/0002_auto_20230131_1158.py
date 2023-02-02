# Generated by Django 2.2.6 on 2023-01-31 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('RO', 'Рок'), ('E', 'Электроника'), ('P', 'Поп'), ('C', 'Классика'), ('F', 'Фолк'), ('CO', 'Кантри'), ('B', 'Блюз'), ('F', 'Фолк'), ('SH', 'Шансон'), ('H', 'Хип-поп'), ('RA', 'Регги'), ('D', 'Диско'), ('O', 'Другое')], default='О', max_length=2)),
            ],
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('text', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Author')),
                ('author_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='music', to=settings.AUTH_USER_MODEL)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Genre')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]
