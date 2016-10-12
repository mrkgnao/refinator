from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

# Examples:
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^', include('refinator.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
