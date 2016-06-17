from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from common_blog.models import Article, Comment, UserArticle
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from .forms import CommentForm, ArticleForm
from django.core.exceptions import ObjectDoesNotExist
from django.forms import Form
import json

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
            newuser = registration_form.save()
            registration = auth.authenticate(username=registration_form.cleaned_data['username'],
                                             password=registration_form.cleaned_data['password2'])
            for article in Article.objects.all():
                userarticle = UserArticle(article=article, user=newuser, can_edit=False)
                userarticle.save()
            auth.login(request, registration)

            return redirect('/')
        else:
            args['form'] = registration_form
    return render_to_response('register.html', args)


def articles(request):
    args = {}
    args.update(csrf(request))
    articles = Article.objects.all()
    args['articles'] = articles
    args['username'] = auth.get_user(request).username
    return render_to_response('articles.html', args)


def article(request, article_id):
    comment_form = CommentForm()
    args = {}
    args.update(csrf(request))
    # post = Article.objects.get(id=article_id)
    # args['author'] = auth.models.User.objects.get(id=post.article_author_id)
    try:
        article = Article.objects.get(id=article_id)
        body = article.article_body
        args['article'] = article
        args['article_lines'] = body.split("\n")
        args['comments'] = Comment.objects.filter(comment_article=article_id)
        args['username'] = auth.get_user(request).username
        args['form'] = comment_form.as_p()
        return render_to_response('article.html', args)
    except ObjectDoesNotExist:
        raise Http404


def vote(request, article_id, type):
    if type == "+":
        vote = 1;
    elif type == "-":
        vote = -1
    else:
        return redirect('/')
    try:
        userarticle = UserArticle.objects.get(user=auth.get_user(request),
                                              article_id=article_id)
        article = Article.objects.get(id=article_id)
        if userarticle.vote == 0:
            if vote == 1:
                article.article_likes += vote
            elif vote == -1:
                article.article_dislikes -= vote
        elif userarticle.vote != vote:
            article.article_likes += vote
            article.article_dislikes -= vote
        article.save()
        userarticle.vote = vote
        userarticle.save()
        data = json.dumps({"likes": article.article_likes,
                           "dislikes": article.article_dislikes,
                           "voted": userarticle.vote == vote})
        return HttpResponse(data)
    except ObjectDoesNotExist:
        raise Http404


def add_article(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article_to_add = form.save(commit=False)
        article_to_add.article_author = auth.get_user(request)
        annotation = form.data["article_body"].strip("\n").split("\n")[0]
        article_to_add.article_annotation = annotation
        form.save()
        for user in auth.models.User.objects.all():
            userarticle = UserArticle(article=article_to_add, user=user,
                                      can_edit=(user == auth.get_user(request)))
            userarticle.save()
    return redirect("/articles/%s" % article_to_add.id)


def new_article(request):
    article_form = ArticleForm()
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['form'] = article_form.as_p()
    return render_to_response('add_article.html', args)


def add_comment(request, article_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.comment_article = Article.objects.get(id=article_id)
        comment.comment_author = auth.get_user(request)
        form.save()
    return redirect('/articles/%s/' % article_id)



