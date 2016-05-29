from django.contrib import admin
from .models import Comment, Article, UserArticle
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title', 'article_body', 'article_date']

admin.site.register(Comment)
admin.site.register(UserArticle)
admin.site.register(Article, ArticleAdmin)