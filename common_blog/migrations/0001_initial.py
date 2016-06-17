# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-06-16 15:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200, verbose_name='Название статьи')),
                ('article_body', models.TextField(verbose_name='Текст статьи')),
                ('article_annotation', models.TextField()),
                ('article_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('article_likes', models.IntegerField(default=0)),
                ('article_dislikes', models.IntegerField(default=0)),
                ('article_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_body', models.TextField(verbose_name='Текст комментария')),
                ('comment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_blog.Article')),
                ('comment_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='UserArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_edit', models.BooleanField()),
                ('vote', models.IntegerField(default=0)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common_blog.Article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_article',
            },
        ),
        migrations.AlterUniqueTogether(
            name='userarticle',
            unique_together=set([('user', 'article')]),
        ),
    ]
