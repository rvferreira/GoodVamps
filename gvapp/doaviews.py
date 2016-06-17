from django.template import loader, RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf


@csrf_protect
def cadastro_doador(request):
    if request.method == 'POST':
        print "tenta cadastro doador"
   
        return HttpResponse("ok doador")
        
    else:
    
        template = loader.get_template('cadastro_doador.html')
        context = {
            'page_title': 'Cadastro Doador'
        }
        context.update(csrf(request))
    
    return HttpResponse(template.render(context))