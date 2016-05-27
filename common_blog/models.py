from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    class Meta():
        db_table = 'article'

    article_title = models.CharField(max_length=200)
    article_body = models.TextField()
    article_date = models.DateTimeField()
    article_likes = models.IntegerField(default=0)
    article_dislikes = models.IntegerField(default=0)

class User(models.Model):
    class Meta():
        db_table = 'user'

    user_name = models.CharField(max_length=100)
    user_password_hash = models.CharField(max_length=200)
    user_email = models.EmailField()
    user_rating = models.IntegerField(default=0)
    user_confirmed = models.BooleanField(default=False)


class Comment(models.Model):
    class Meta():
        db_table = 'comment'

    comment_body = models.TextField()
    comment_article = models.ForeignKey(Article)
    comment_author = models.ForeignKey(User)

class UserArticle(models.Model):
    user = models.ForeignKey(User)
    article = models.ForeignKey(Article)
    role = models.IntegerField() #  like in POSIX API : can read = 4(always), can edit = 2, author 1
    vote = models.IntegerField(default=0) #  +1; -1; not voted -- 0
    class Meta():
        db_table = 'user_article'
        unique_together = (('user','article'),)


