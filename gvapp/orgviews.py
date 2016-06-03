from django.template import loader, RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf


@csrf_protect
def cadastro_organizador(request):
    if request.method == 'POST':
        
        uname = request.POST.get('uname', '')
        
        if uname:
            template = loader.get_template('cadastro_organizador_2.html')
            context = {
                'page_title': 'Cadastro Organizador',
                'uname': uname,
                'password': request.POST.get('password')
            }
            context.update(csrf(request))
        
            return HttpResponse(template.render(context))
        
    else:
    
        template = loader.get_template('cadastro_organizador.html')
        context = {
            'page_title': 'Cadastro Organizador'
        }
        context.update(csrf(request))
    
        return HttpResponse(template.render(context))