from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cadastro/$', views.cadastro, name='Cadastro'),
    url(r'^organizador/cadastro/$', views.cadastro_org, name='Cadastro'),
    url(r'^campanhas/$', views.campanhas, name='campanhas'),
    url(r'^campanhas/details/$', views.campanha_details, name='campanha_details'),
    url(r'^$', views.index, name="index"),
]