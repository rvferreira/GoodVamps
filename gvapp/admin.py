from django.contrib import admin
from models import Doador, Organizador, Campanha, DoadorCampanha

# Register your models here.
admin.site.register(Doador)
admin.site.register(Organizador)
admin.site.register(Campanha)
admin.site.register(DoadorCampanha)
