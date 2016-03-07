from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^pikachu/$', views.index, name='index'),
	url(r'^login/$', views.login, name='login'),
    url(r'^login_check/$', views.login_check, name='login_check'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^registration_check/$', views.registration_check, name='registration_check'),
    url(r'^home/$', views.home, name='home'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^forgotpwd/$', views.forgotpwd, name='forgotpwd'),
    url(r'^regAdmin/$', views.regAdmin, name='regAdmin'),
    url(r'^regAdminHome/$', views.regAdminHome, name='regAdmin_checkHome'),
    url(r'^regAdmin_check/$', views.regAdminCheck, name='regAdmin_check'),
	)