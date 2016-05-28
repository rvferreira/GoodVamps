from django.template import loader, RequestContext
from django.http import HttpResponse

from models import Campanha

def index(request):
	template = loader.get_template('base.html')
	context = RequestContext(request, {
		'page_title': 'Home',
	})

	return HttpResponse(template.render(context))

def campanhas(request):
	all_entrys = Campanha.objects.all()
	
	template = loader.get_template('campanhas.html')
	context = RequestContext(request, {
		'page_title': 'Campanhas',
		'campanhas': all_entrys,
	})

	return HttpResponse(template.render(context))