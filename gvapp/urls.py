from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^campanhas/$', views.campanhas, name='campanhas'),
    url(r'^cadastro/$', views.cadastro, name='Cadastro'),
    url(r'^organizador/cadastro/$', views.cadastro_organizador, name='Cadastro'),
    url(r'^organizador/login/$', views.login_organizador, name='Login'),
    url(r'^organizador/logout/$', views.logout_organizador, name='Logout'),
    url(r'^campanhas/details/$', views.campanha_details, name='campanha_details'),
    url(r'^campanhas/', views.campanhas, name='campanhas'),
    url(r'^doador/cancela_participacao', views.cancel_part_camp, name='cancela_participacao'),
    url(r'^doador/', views.profile_doador, name='profile_doador'),
    url(r'^organizador/cadastro_campanha', views.cadastro_campanha, name='cadastro_campanha'),
    url(r'^organizador/cancela_campanha', views.cancela_campanha, name='cancela_campanha'),
    url(r'^organizador/', views.profile_organizador, name='profile_organizador'),
    url(r'^$', views.index, name="index"),
]