from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from common_blog.models import Article, Comment
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf


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
    args['article'] = Article.objects.all
    args['username'] = auth.get_user(request).username
    return render_to_response('articles.html', args)


def article(request, article_id):
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comment.objects.filter(comments_article_id=article_id)
    args['username'] = auth.get_user(request).username
    return render_to_response('article.html', args)