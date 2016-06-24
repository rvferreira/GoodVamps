from django.template import loader, RequestContext
from django.http import HttpResponse, JsonResponse
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_protect
from django.template.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime   
from models import Organizador, Campanha

@csrf_protect
def login_organizador(request):
    if request.method == 'POST':
        login = request.POST.get('uname')
        senha = request.POST.get('password')
        
        try:
            user = Organizador.objects.get(login=login, senha=senha)
            request.session["user_id"] = login
            request.session["user_type"] = "organizador"
            
            
            
            return HttpResponse("Sucesso! Voce sera redirecionado para a sua pagina de perfil.")
        
        except ObjectDoesNotExist:
            return HttpResponse("Erro: Credenciais Invalidas!")
        
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        return profile_organizador(request, user_id);
        
    template = loader.get_template("login.html")
    context = {
        'page_title': 'Login de Organizador',
    }
    context.update(csrf(request))
    
    return HttpResponse(template.render(context))

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
    }
    context.update(csrf(request))

    return HttpResponse(template.render(context))

def profile_organizador(request, user=None):  
    if not user:
        user = request.session.get("user_id", '')
    
    if not user:
        return login_organizador(request) 
    
    template = loader.get_template('profile_organizador.html')
    org_entry = Organizador.objects.get(login=user)
    org_all_entrys = Campanha.objects.all().filter(organizador=user)
    context = {
        'page_title': 'Home',
        'campanhas': org_all_entrys,
        'organizador': org_entry,
        'full_url': request.get_full_path,
    }
    
    return HttpResponse(template.render(context))
