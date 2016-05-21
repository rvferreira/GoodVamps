from django.template import loader, RequestContext
from django.http import HttpResponse

# Create your views here.
def index(request):

	template = loader.get_template('base.html')
	context = RequestContext(request, {
		'page_title': 'Home',
	})

	return HttpResponse(template.render(context))