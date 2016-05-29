"""GoodVamps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.views.generic import RedirectView, TemplateView

#temporary: for serving static files
#TODO: remove static url serving in production
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^team/', TemplateView.as_view(template_name='team.html'), name="team"),
    url(r'^who/', TemplateView.as_view(template_name='who.html'), name="who"),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('gvapp.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
