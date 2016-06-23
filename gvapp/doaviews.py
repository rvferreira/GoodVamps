from django.template import loader, RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf


@csrf_protect
def cadastro_doador(request):

    if request.method == 'POST':
        
        step = request.POST.get('step', '')
        #fbUserId = request.POST.get('fbUserId', '')

        #return HttpResponse("user id= "+fbUserId)

        if step == '1':

            template = loader.get_template('cadastro_doador_2.html')
            context = {
                'page_title': 'Cadastro Organizador',
            }
            context.update(csrf(request))

            return HttpResponse(template.render(context))
            
        elif step =='2':
            return HttpResponse("step 2!")
        
    template = loader.get_template('cadastro_doador.html')
    context = {
        'page_title': 'Cadastro Doador',
    }
    context.update(csrf(request))

    return HttpResponse(template.render(context))