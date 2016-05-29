from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from common_blog.models import Article, Comment, UserArticle
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from .forms import CommentForm, ArticleForm

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('login.html', args)

    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect("/")


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        registration_form = UserCreationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            registration = auth.authenticate(username=registration_form.cleaned_data['username'],
                                             password=registration_form.cleaned_data['password2'])
            auth.login(request, registration)
            return redirect('/')
        else:
            args['form'] = registration_form
    return render_to_response('register.html', args)


def articles(request):
    args = {}
    args.update(csrf(request))
    args['articles'] = Article.objects.all()
    args['username'] = auth.get_user(request).username
    return render_to_response('articles.html', args)


def article(request, article_id):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
  #  user_article = UserArticle.objects.get(article=article_id)
  #  args['author'] = UserArticle.objects.get(user=user_article.id)
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comment.objects.filter(comment_article=article_id)
    args['username'] = auth.get_user(request).username
    args['form'] = comment_form
    return render_to_response('article.html', args)


# TODO: like, dislike, addarticle


def like(request, article_id):
    pass


def dislike(request, article_id):
    pass


def addarticle(request):
    form = ArticleForm(request.POST)
    return redirect('/')


def newarticle(request):
    article_form = ArticleForm
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['form'] = article_form
    return render_to_response('add_article.html', args)


def addcomment(request, article_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.comment_article = Article.objects.get(id=article_id)
        comment.comment_author = auth.get_user(request)
        form.save()
    return redirect('/articles/%s/' % article_id)


