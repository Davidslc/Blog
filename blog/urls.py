from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    # url(r'^$', views.post_list),
    url(r'^posts/$', views.PostList.as_view(), name='post_list'),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post_detail'),
    #url(r'^posts/new/$', views.post_new, name='post_new'),
    #url(r'^posts/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
)
