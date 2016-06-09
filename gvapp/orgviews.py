from django.template import loader, RequestContext
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.template.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
from models import Organizador


@csrf_protect
def cadastro_organizador(request):

    if request.method == 'POST':
        
        step = request.POST.get('step', '')
        if step == "1":
            
            try: 
                uname = request.POST.get('uname')
                Organizador.objects.get(login=uname)
                return JsonResponse({"error":"Nome de usuario ja existe"})
                
            except ObjectDoesNotExist:
                template = loader.get_template('cadastro_organizador_2.html')
                context = {
                    'page_title': 'Cadastro Organizador',
                    'uname': uname,
                    'password': request.POST.get('password')
                }
                context.update(csrf(request))

                return HttpResponse(template.render(context))
        
        elif step =='2':
            login = request.POST.get('uname')
            senha = request.POST.get('password')
            site = request.POST.get('site')
            telefone = request.POST.get('telefone')
            nome = request.POST.get('organizacao')
            responsavel = request.POST.get('responsavel')
            localizacao = request.POST.get('endereco')
            email = request.POST.get('email')
            
            new_entry = Organizador(login=login, senha=senha, site=site, telefone=telefone,
                                    nome=nome, responsavel=responsavel, localizacao=localizacao, email=email)
            new_entry.save()
            
            return HttpResponse("Concluido!")
        
    template = loader.get_template('cadastro_organizador.html')
    context = {
        'page_title': 'Cadastro Organizador',
        'error_msg': 'Username already taken'
    }
    context.update(csrf(request))

    return HttpResponse(template.render(context))