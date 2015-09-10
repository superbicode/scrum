from django.conf.urls import patterns, url

from scrum import views

urlpatterns = patterns('',
    # ex: /scrum/
    url(r'^$', views.index, name='index'),
    # ex: /scrum/2/
    url(r'^(?P<task_id>\d+)/$', views.detail, name='detail'),
    # ex: /scrum/5/results/
    url(r'^(?P<task_id>\d+)/assign/$', views.assign, name='assign'),
    # ex: /scrum/5/active/
    url(r'^(?P<task_id>\d+)/status/$', views.status, name='status'),

)