from django.conf.urls import url

from . import views

app_name = 'refinator'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<ref_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<ref_id>[0-9]+)/vote/(?P<vote_type>(up|down))/$', views.vote, name='vote'),
]	
