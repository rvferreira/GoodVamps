from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^campanhas/$', views.campanhas, name='campanhas'),
    url(r'^$', views.index, name="index"),
]