from django.template import loader, RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def cadastro_organizador(request):
    if request.method == 'POST':
        print "tenta cadastro"
   
        return HttpResponse(context_instance=RequestContext(request))
        
    else:
    
        template = loader.get_template('cadastro_organizador.html')
        context = {
            'page_title': 'Cadastro Organizador'
        }
    
    return HttpResponse(template.render(context))