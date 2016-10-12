from django.conf.urls import url
from django.contrib.auth.views import login, logout

from .views import references, tags, create_user, static_pages

app_name = 'refinator'

urlpatterns = [
    url(r'^about/$', static_pages.about, name='about'),
    url(r'^contact/$', static_pages.contact, name='contact'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^refs/new/$', references.ref_edit, name='ref_create'),
    url(r'^refs/edit/(?P<ref_id>[0-9]+)/$',
        references.ref_edit,
        name='ref_edit'),
    url(r'^$', lambda req: references.ref_index(req, 1), name='ref_index'),
    url(r'^refs/page/(?P<page_no>[0-9]+)/$',
        references.ref_index,
        name='ref_index_paged'),
    url(r'^refs/(?P<ref_id>[0-9]+)/$',
        references.ref_detail,
        name='ref_detail'),
    url(r'^refs/(?P<ref_id>[0-9]+)/vote/(?P<vote_type>(up|down))/$',
        references.ref_vote,
        name='ref_vote'),
    url(r'^tags/new/$', tags.tag_edit, name='tag_create'),
    url(r'^tags/edit/(?P<tag_id>[0-9]+)/$', tags.tag_edit, name='tag_edit'),
    url(r'^tags/$', lambda req: tags.tag_index(req, 1), name='tag_index'),
    url(r'^tags/page/(?P<page_no>[0-9]+)/$',
        tags.tag_index,
        name='tag_index_paged'),
    url(r'^tags/(?P<tag_id>[0-9]+)/$', tags.tag_detail, name='tag_detail'),

    # Registration
    url(r'^register/$', create_user.register, name='register'),
    url(r'^register/complete/$',
        create_user.registration_complete,
        name='registration_complete'),
]
