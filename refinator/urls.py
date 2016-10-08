from django.conf.urls import url

from .views import references, tags

app_name = 'refinator'

urlpatterns = [
    url(r'^$', references.ref_index, name='ref_index'),
    url(r'^(?P<ref_id>[0-9]+)/$', references.ref_detail, name='ref_detail'),
    url(r'^(?P<ref_id>[0-9]+)/vote/(?P<vote_type>(up|down))/$', references.ref_vote, name='ref_vote'),

    url(r'^tags/$', tags.tag_index, name='tag_index'),
    url(r'^tags/(?P<tag_id>[0-9]+)/$', tags.tag_detail, name='tag_detail'),
]	
