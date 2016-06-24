from django.template import loader, RequestContext
from django.http import HttpResponse, JsonResponse
from models import Doador
from models import Campanha

def profile_doador(request):	
	nome = 'Jessika Darambaris'
	doa_entry = Doador.objects.get(nome=nome)
	doa_all_entrys = Campanha.objects.all().filter(doadores=doa_entry)
	if nome:
		template = loader.get_template('profile_doador.html')
		context = {
			'page_title': 'Home',
			'doador': doa_entry,
			'campanhas': doa_all_entrys
		}

	return HttpResponse(template.render(context))

