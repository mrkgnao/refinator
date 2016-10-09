from django.conf.urls import url
from django.contrib.auth.views import login, logout

from .views import references, tags, create_user

app_name = 'refinator'

urlpatterns = [
    url(r'^$', references.ref_index, name='ref_index'),

    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),

    url(r'^(?P<ref_id>[0-9]+)/$', references.ref_detail, name='ref_detail'),
    url(r'^(?P<ref_id>[0-9]+)/vote/(?P<vote_type>(up|down))/$', references.ref_vote, name='ref_vote'),

    url(r'^tags/$', tags.tag_index, name='tag_index'),
    url(r'^tags/(?P<tag_id>[0-9]+)/$', tags.tag_detail, name='tag_detail'),

    # Registration
    url(r'^register/$', create_user.register, name='register'),
    url(r'^register/complete/$', create_user.registration_complete, name='registration_complete'),

]
