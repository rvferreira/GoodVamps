from django.template import loader, RequestContext
from django.http import HttpResponse, JsonResponse
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from orgviews import cadastro_organizador, login_organizador, profile_organizador
from doaviews import cadastro_doador_1, cadastro_doador_2, login_doador, profile_doador
from models import Campanha, Organizador, Doador, DoadorCampanha

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
	campanha = Campanha.objects.get(cod=request.GET.get('cod'))
	
	participando = 0
	
	try:
		doador = Doador.objects.get(fb_user_id=request.session.get('user_id', ''))
		entry = DoadorCampanha.objects.get(doador=doador, campanha=campanha)
		participando = 1
	except ObjectDoesNotExist:
		pass
	
	template = loader.get_template('campanha_detail.html')
	context = RequestContext(request, {
		'campanha': campanha,
		'participando': participando
	})

	return HttpResponse(template.render(context))

@csrf_protect
def cadastro_campanha(request, user=None):
	if not user: 
		user = request.session.get("user_id",'')

	if not user:
		return login_organizador(request)

	organizador = Organizador.objects.get(login=user)
	opcoes_sangue = (('O-', 'O-'), ('O+', 'O+'), ('A-', 'A-'), ('A+', 'A+'), ('B-', 'B-'), ('B+', 'B+'), ('AB-', 'AB-'), ('AB+', 'AB+'))
	
	try:
		nome = request.POST.get('nome')
		localizacao = request.POST.get('localizacao')
		Campanha.objects.get(nome=nome,localizacao=localizacao)
		return JsonResponse({"error":"Campanha ja cadastrada"})	

	except ObjectDoesNotExist:
		nome = request.POST.get('nome')
		localizacao = request.POST.get("localizacao")
		tipo_prioritario = request.POST.get("grupo_sanguineo")
		data = request.POST.get("data")
		print tipo_prioritario

		inicio = datetime.strptime(data, "%d %B, %Y")
		fim = datetime.strptime(data, "%d %B, %Y")

		new_entry = Campanha(nome=nome,localizacao=localizacao,inicio=inicio,fim=fim,organizador=organizador,tipo_prioritario=tipo_prioritario)		
		new_entry.save()
		return HttpResponse('success')
	

def cancela_campanha(request, user=None):
	if not user: 
		user = request.session.get("user_id",'')

	if not user:
		return login_organizador(request)

	idcampanha = request.GET.get('idcampanha')
	campanha = Campanha.objects.get(cod=idcampanha)
	campanha.delete()
	
	return HttpResponse('success')
	
def cancel_part_camp(request):

	idcampanha = request.GET.get('idcampanha')
	nome = request.GET.get('namedoador')
	campanha = Campanha.objects.get(cod=idcampanha)
	doador = Doador.objects.get(nome=nome)
	if doador:
		doacao = DoadorCampanha.objects.get(doador=doador,campanha=campanha)
		doacao.delete()
		return HttpResponse('success')
	else:
		return (login_organizador)	

def part_camp(request):
	idcampanha = request.POST.get('id_campanha', '')
	nome = request.POST.get('id_doador', '')
	campanha = Campanha.objects.get(cod=idcampanha)
	doador = Doador.objects.get(fb_user_id=nome)
	
	try:
		entry = DoadorCampanha.objects.get(doador=doador, campanha=campanha)
	except ObjectDoesNotExist:
		if doador:
			doacao = DoadorCampanha.objects.create(doador=doador,campanha=campanha)
			return HttpResponse('success')
		else:
			return (login_organizador)	
	
	return HttpResponse('replicated')

def cadastro_org(request):	
	template = loader.get_template('cadastro_organizador.html')
	context = RequestContext(request, {
		'page_title': 'Cadastro',
	})

	return HttpResponse(template.render(context))

def cadastro(request):	
	template = loader.get_template('signup.html')
	context = {
		'page_title': 'Cadastro',
	}
	
	return HttpResponse(template.render(context))

def logout(request):
    try:
        del request.session["user_id"]
        del request.session["user_type"]
    except KeyError:
        pass
    
    return index(request)

