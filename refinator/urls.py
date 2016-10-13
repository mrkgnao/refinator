from django.conf.urls import url
from django.contrib.auth.views import login, logout

from .views import references, tags, create_user, static_pages

app_name = 'refinator'

urlpatterns = [
    url(r'^about/$', static_pages.about, name='about'),
    url(r'^contact/$', static_pages.contact, name='contact'),
    url(r'^login/$', login, {'template_name': 'registration/login.djhtml'}, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^register/$', create_user.register, name='register'),

    #
    # refs
    #

    url(r'^refs/new/$', references.ref_edit, name='ref_create'),
    url(r'^refs/edit/(?P<ref_id>[0-9]+)/$',
        references.ref_edit,
        name='ref_edit'),

    #
    # ref index and search
    #

    # TODO make landing page
    url(r'^$', references.search),
    url(r'^refs/$', references.search, name='ref_index'),
    url(r'^refs/page/(?P<page_no>[0-9]+)/$', references.search),
    url(r'^refs/search/$', references.search, name='ref_search'),
    url(r'^refs/search/(?P<query>[a-zA-Z0-9]*)/$', references.search),
    url(r'^refs/search/(?P<query>[a-zA-Z0-9]*)/page/(?P<page_no>[0-9]+)/$',
        references.search),
    #
    # detail
    #
    url(r'^refs/(?P<ref_id>[0-9]+)/$',
        references.ref_detail,
        name='ref_detail'),
    url(r'^refs/(?P<ref_id>[0-9]+)/vote/(?P<vote_type>(up|down))/$',
        references.ref_vote,
        name='ref_vote'),
    #
    # tags
    #

    url(r'^tags/new/$', tags.tag_edit, name='tag_create'),
    url(r'^tags/edit/(?P<tag_id>[0-9]+)/$',
        tags.tag_edit,
        name='tag_edit'),

    url(r'^$', tags.search),
    url(r'^tags/$', tags.search, name='tag_index'),
    url(r'^tags/page/(?P<page_no>[0-9]+)/$', tags.search),
    url(r'^tags/search/$', tags.search, name='tag_search'),
    url(r'^tags/search/(?P<query>[a-zA-Z0-9]*)/$', tags.search),
    url(r'^tags/search/(?P<query>[a-zA-Z0-9]*)/page/(?P<page_no>[0-9]+)/$',
        tags.search),
    url(r'^tags/(?P<tag_id>[0-9]+)/$',
        tags.detail,
        name='tag_detail'),
]
