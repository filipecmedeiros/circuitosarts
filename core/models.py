from django.db import models

# Create your models here.

class State (models.Model):
	name = models.CharField('Estado', max_length=100)

	def __str__ (self):
		return self.name
	
	class Meta:
		verbose_name = 'Estado'
		verbose_name_plural = 'Estados'
		ordering = ['name']

class City (models.Model):
	name = models.CharField ('Cidade', max_length=100)
	state = models.ForeignKey('core.State', verbose_name='Estado')

	def __str__ (self):
		return self.name

	class Meta:
		verbose_name = 'Cidade'
		verbose_name_plural = 'Cidades'
		ordering = ['state', 'name']

class Style (models.Model):

	gener = models.CharField ('Gênero', max_length=100)
	
	def __str__ (self):
		return self.gener

	class Meta:
		verbose_name = 'Gênero'
		verbose_name_plural = 'Gêneros'
		ordering = ['gener']

class Artist (models.Model):

	name = models.CharField('Nome', max_length=100)
	gener = models.ForeignKey('core.Style', verbose_name='Gênero')

	state = models.ForeignKey('core.State', verbose_name='Estado')
	city = models.ForeignKey('core.City', verbose_name='Cidade')
	neighborhood = models.CharField ('Bairro', max_length=100)
	address = models.CharField('Endereço', max_length=200)

	price = models.IntegerField ('Cachê')
	contact = models.CharField('Contato', max_length=100)

	created = models.DateTimeField ('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	def __str__ (self):
		return self.name

	class Meta:
		verbose_name = 'Artista'
		verbose_name_plural = 'Artistas'
		ordering = ['state', 'city', 'neighborhood', 'name']

class Club (models.Model):

	name = models.CharField('Nome', max_length=100)
	owner = models.CharField('Responsável', max_length=100)
	opened = models.CharField('Horário de funcionamento', max_length=100)

	state = models.ForeignKey('core.State', verbose_name='Estado')
	city = models.ForeignKey('core.City', verbose_name='Cidade')
	neighborhood = models.CharField('Bairro', max_length=100)
	address = models.CharField('Endereço', max_length=200)

	contact = models.CharField('Contato', max_length=100)

	created = models.DateTimeField ('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	def __str__ (self):
		return self.name

	class Meta:
		verbose_name = 'Espaço'
		verbose_name_plural = 'Espaços'
		ordering = ['state', 'city', 'name']
