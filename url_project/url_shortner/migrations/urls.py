from django.conf.urls import patterns, url
from url_shortner import views

urlpatterns = patterns('',
        url(r'^$', views.home, name='home'),
        url(r'^redirect/$', views.redirect_orignal, name='redirect'))
