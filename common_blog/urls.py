from django.conf.urls import include, url
from . import views

urlpatterns = [

  url(r'^$', views.articles),
  url(r'articles/(?P<article_id>\d+)/$', views.article),


  url(r'^login/$', views.login),
  url(r'^logout/$', views.logout),
  url(r'^register/$', views.register),

]
