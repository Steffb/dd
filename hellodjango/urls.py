from django.conf.urls import patterns, include, url
from hellodjango.views import *
from django.contrib import admin
from rss.views import rss3

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hellodjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/$',test),
)
