from django.template import loader, RequestContext
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.template.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from models import Doador, Campanha
from views import login_organizador

def profile_doador(request, user=None):	
	if not user:
		user = request.session.get("user_id", '')
    
	if not user:
		return login_organizador(request) 
	
	doa_entry = Doador.objects.get(fb_user_id=user)
	doa_all_entrys = Campanha.objects.all().filter(doadores=doa_entry)
	
	template = loader.get_template('profile_doador.html')
	context = {
		'page_title': 'Home',
		'doador': doa_entry,
		'campanhas': doa_all_entrys,
	}
	
	return HttpResponse(template.render(context))

@csrf_protect
def login_doador(request):
    fbUserId = request.POST.get('facebookId')
    
    request.session["user_id"] = fbUserId
    request.session["user_type"] = "doador"
    
    return JsonResponse({"status":"success"})

@csrf_protect
def cadastro_doador_2(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        location = request.POST.get('location')
        birthdate = datetime.strptime(request.POST.get('birthdate'), "%m/%d/%Y")
        gender = request.POST.get('gender')
        bloodtype = request.POST.get('bloodtype')
        lastdonation = request.POST.get('lastdonation')
        fbUserId = request.POST.get('facebookId')
        
        try: 
            Doador.objects.get(fb_user_id=fbUserId)
            return JsonResponse({"error":"Usuario ja cadastrado"})
        
        except ObjectDoesNotExist:
            new_entry = Doador(nome = name, email = email, localizacao = location, nascimento = birthdate,
                               sexo = gender, tipo_sanguineo = bloodtype, ultima_doacao = lastdonation, fb_user_id = fbUserId)
            new_entry.save()

        return HttpResponse("ok")
        
    template = loader.get_template('cadastro_doador_2.html')
    context = {
        'page_title': 'Cadastro Doador',
    }
    context.update(csrf(request))

    return HttpResponse(template.render(context))

def cadastro_doador_1(request):
    template = loader.get_template('cadastro_doador.html')
    context = {
        'page_title': 'Cadastro Doador',
    }
    context.update(csrf(request))

    return HttpResponse(template.render(context))
