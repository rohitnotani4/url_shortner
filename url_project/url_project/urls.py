from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from url_shortner import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'url_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.cover_page, name='cover_page'),
    url(r'^url_shortner/', include('url_shortner.urls'), name='short_url_form'),
    url(r'^admin/', include(admin.site.urls)),
)
