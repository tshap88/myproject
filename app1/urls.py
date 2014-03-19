from django.conf.urls import patterns, url

from app1 import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<appaction>.*)/$', views.detail, name='detail'),
#    url(r'^(?P<.......>.*)/$', views.end, name='end'),
)