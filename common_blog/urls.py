from django.conf.urls import include, url
from . import views

urlpatterns = [

  url(r'articles/$', views.articles),
  url(r'articles/(?P<article_id>\d+)/$', views.article)
]
