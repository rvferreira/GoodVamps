from django.template import loader, RequestContext
from django.http import HttpResponse

def index(request):
	template = loader.get_template('base.html')
	context = RequestContext(request, {
		'page_title': 'Home',
	})

	return HttpResponse(template.render(context))

def campanhas(request):
	template = loader.get_template('base.html')
	context = RequestContext(request, {
		'page_title': 'Campanhas',
	})

	return HttpResponse(template.render(context))