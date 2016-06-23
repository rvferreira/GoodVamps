def home_doador(request):	
	user = ''
	template = loader.get_template('home_doador.html')
	context = {
		'page_title': 'Home',
	}

	return HttpResponse(template.render(context))

