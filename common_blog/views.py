from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from common_blog.models import Article, Comment
# Create your views here.


def articles(request):
    return render_to_response('articles.html', {'articles': Article.objects.all()})


def article(request, article_id):
    return render_to_response('article.html', {'article': Article.objects.get(id=article_id),
                                               'comments': Comment.objects.filter(comment_article=article_id)})
