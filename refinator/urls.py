from django.conf.urls import url

from .views import references

app_name = 'refinator'

urlpatterns = [
    url(r'^$', references.index, name='index'),
    url(r'^(?P<ref_id>[0-9]+)/$', references.detail, name='detail'),
    url(r'^(?P<ref_id>[0-9]+)/vote/(?P<vote_type>(up|down))/$', references.vote, name='vote'),
]	
