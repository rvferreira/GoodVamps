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
		'full_url': request.get_full_path,
	})

	return HttpResponse(template.render(context))

def campanha_details(request):
	entry = Campanha.objects.get(cod=request.GET.get('cod'))
	
	template = loader.get_template('campanha_detail.html')
	context = RequestContext(request, {
		'campanha': entry,
	})

	return HttpResponse(template.render(context))

def cadastro_org(request):	
	template = loader.get_template('cadastro_organizador.html')
	context = RequestContext(request, {
		'page_title': 'Cadastro',
	})

	return HttpResponse(template.render(context))

def cadastro(request):	
	template = loader.get_template('signup.html')
	context = RequestContext(request, {
		'page_title': 'Cadastro',
	})

	return HttpResponse(template.render(context))