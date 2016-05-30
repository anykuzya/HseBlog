# -*- coding: utf-8 -*-

from django.forms import ModelForm
from .models import Comment, Article


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_body']


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['article_title', 'article_body']
