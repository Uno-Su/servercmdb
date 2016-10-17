# encoding: utf-8
# author=wenbin.su

from django.conf.urls import url
from .views import index, Login, Logout, signup

urlpatterns = [
    url(r'^$', index, name="index"),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', vote, name='vote'),
    # url(r'^(?P<question_id>[0-9]+)/$', detail, name='detail'),
    # url(r'^(?P<question_id>[0-9]+)/results/$', results, name='results'),
    url(r'^login/$', Login, name='login'),
    url(r'^logout/$', Logout, name='logout'),
    url(r'^signup/$', signup, name='signup'),
]