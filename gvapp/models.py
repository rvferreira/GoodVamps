from django.db import models
from django.utils import timezone

class Doador(models.Model):
	opcoes_sexo = (('M', 'Masculino'),('F', 'Feminino'))
	opcoes_sangue = (('O-', 'O-'), ('O+', 'O+'), ('A-', 'A-'), ('A+', 'A+'), ('B-', 'B-'), ('B+', 'B+'), ('AB-', 'AB-'), ('AB+', 'AB+'))

	nome = models.CharField(max_length = 200)
	email = models.EmailField(max_length = 100, primary_key = True)
	localizacao = models.CharField(max_length = 50)
	nascimento = models.DateField(auto_now = False, auto_now_add = False);
	sexo = models.CharField(max_length = 1, choices = opcoes_sexo, blank = True)
	tipo_sanguineo = models.CharField(max_length = 3, choices = opcoes_sangue, blank = True)
	ultima_doacao = models.CharField(max_length = 3)
	fb_user_id = models.CharField(max_length = 100)
	
	def __unicode__(self):
		return "Doador: " + self.nome

class Organizador(models.Model):
	login = models.CharField(max_length = 50, primary_key = True)
	senha = models.CharField(max_length = 50)
	site = models.CharField(max_length = 50)
	telefone = models.CharField(max_length = 20, null = True)
	nome = models.CharField(max_length = 200)
	responsavel = models.CharField(max_length = 200)
	localizacao = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 100)
	
	def __unicode__(self):
		return "Organizador: " + self.nome

class Campanha(models.Model):
	opcoes_sangue = (('O-', 'O-'), ('O+', 'O+'), ('A-', 'A-'), ('A+', 'A+'), ('B-', 'B-'), ('B+', 'B+'), ('AB-', 'AB-'), ('AB+', 'AB+'))

	cod = models.AutoField(primary_key = True)
	nome = models.CharField(max_length = 50)
	localizacao = models.CharField(max_length = 50)
	inicio = models.DateField()
	fim = models.DateField()
	organizador = models.ForeignKey('Organizador', on_delete = models.CASCADE)
	tipo_prioritario = models.CharField(max_length = 3, choices = opcoes_sangue, blank = True)
	doadores = models.ManyToManyField(Doador, through = 'DoadorCampanha')
	
	def __unicode__(self):
		return "Campanha: " + self.nome

class DoadorCampanha(models.Model):
	doador = models.ForeignKey('Doador', on_delete = models.CASCADE)
	campanha = models.ForeignKey('Campanha', on_delete = models.CASCADE)
