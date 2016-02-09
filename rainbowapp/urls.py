from django.conf.urls import  patterns, include, url
from . import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
	url(r'^pikachu/$', views.home, name='home'),
	url(r'^login/$', views.login, name='login'),
    url(r'^login_check/$', views.login_check, name='login_check'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^registration_check/$', views.registration_check, name='registration_check'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^forgotpwd/$', views.forgotpwd, name='forgotpwd'),
	)