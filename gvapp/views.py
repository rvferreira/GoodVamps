from django.template import loader, RequestContext
from django.http import HttpResponse
from orgviews import cadastro_organizador
from datetime import datetime

from models import Campanha

def index(request):
	template = loader.get_template('index.html')
	context = RequestContext(request, {
		'page_title': 'Home',
	})

	return HttpResponse(template.render(context))

def campanhas(request):	
	local = request.GET.get('local', '');
	data = request.GET.get('data', '');
	
	all_entrys = Campanha.objects.all().filter(fim__gte=datetime.today())
	
	if local:
		all_entrys = all_entrys.filter(localizacao__icontains=local)
		
	if data:
		all_entrys = all_entrys.filter(inicio__lte=datetime.strptime(data, "%d %B, %Y"))
		all_entrys = all_entrys.filter(fim__gte=datetime.strptime(data, "%d %B, %Y"))
	
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