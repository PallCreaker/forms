# create fujita

from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /froms/ name="function name of views"
    url(r'^$', views.index, name='index'),
    # ex: /forms/5/ question_id = 引数 of views
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /forms/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /forms/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    # not recommended
    # url(r'^polls/latest\.html$', views.index),
]
