from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^doador/cadastro/$', views.cadastro_doador, name = 'Cadastro Doador'),
    url(r'^organizador/cadastro/$', views.cadastro_organizador, name='Cadastro'),
    url(r'^campanhas/$', views.campanhas, name='campanhas'),
    url(r'^campanhas/details/$', views.campanha_details, name='campanha_details'),
    url(r'^$', views.index, name="index"),
]