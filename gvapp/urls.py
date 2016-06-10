from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^organizador/cadastro/$', views.cadastro_organizador, name='Cadastro'),
    url(r'^organizador/login/$', views.login_organizador, name='Login'),
    url(r'^organizador/logout/$', views.logout_organizador, name='Logout'),
    url(r'^campanhas/details/$', views.campanha_details, name='campanha_details'),
    url(r'^campanhas/', views.campanhas, name='campanhas'),
    url(r'^$', views.index, name="index"),
]