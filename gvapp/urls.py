from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^campanhas/$', views.campanhas, name='campanhas'),
    url(r'^cadastro/$', views.cadastro, name='Cadastro'),
	url(r'^doador/cadastro/1$', views.cadastro_doador_1, name = 'Cadastro Doador'),
	url(r'^doador/cadastro/2$', views.cadastro_doador_2, name = 'Cadastro Doador'),
    url(r'^organizador/cadastro/$', views.cadastro_organizador, name='Cadastro'),
    url(r'^organizador/login/$', views.login_organizador, name='Login'),
    url(r'^organizador/logout/$', views.logout, name='Logout'),
    url(r'^doador/logout/$', views.logout, name='Logout'),
    url(r'^campanhas/details/$', views.campanha_details, name='campanha_details'),
    url(r'^organizador/$', views.profile_organizador, name='profile_organizador'),
    url(r'^$', views.index, name="index"),
]