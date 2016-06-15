from django.conf.urls import include, url
from . import views

urlpatterns = [

  url(r'articles/(?P<article_id>\d+)/$', views.article),

  url(r'^articles/(?P<article_id>\d+)/vote/(?P<type>[+,-]{1})/$', views.vote),
  url(r'^articles/(?P<article_id>\d+)/add_comment/$', views.add_comment),
  url(r'^add_article/$', views.add_article),
  url(r'^new_article/$', views.new_article),
  url(r'^login/$', views.login),
  url(r'^logout/$', views.logout),
  url(r'^register/$', views.register),

  url(r'^articles/$', views.articles),
  url(r'^$', views.articles),

]
