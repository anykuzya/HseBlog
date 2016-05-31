from django.conf.urls import include, url
from . import views

urlpatterns = [

  url(r'articles/(?P<article_id>\d+)/$', views.article),

  url(r'^like/$', views.like, name='like'),
  url(r'^dislike/$', views.dislike, name='dislike'),

  url(r'^articles/(?P<article_id>\d+)/like/$', views.like, name='like'),
  url(r'^articles/(?P<article_id>\d+)/dislike/$', views.dislike),
  url(r'^articles/addcomment/(?P<article_id>\d+)/$', views.addcomment),
  url(r'^addarticle/$', views.addarticle),
  url(r'^newarticle/$', views.newarticle),
  url(r'^login/$', views.login),
  url(r'^logout/$', views.logout),
  url(r'^register/$', views.register),

  url(r'^$', views.articles),

]
