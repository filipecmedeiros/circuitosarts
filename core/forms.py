from django import forms 

from .models import State, City, Style



class ArtistForm (forms.Form):
	
	name = forms.CharField(label='Nome')
	gener = forms.ChoiceField(label='Gênero musical')

	state = forms.ChoiceField(label='Estado')
	city = forms.ChoiceField(label='Cidade')
	neighborhood = forms.CharField(label='Bairro')
	address = forms.CharField(label='Endereço')

	price = forms.IntegerField(label='Cachê')
	contact = forms.CharField(label='Contato')

	def __init__(self, *args, **kwargs):
		super(ArtistForm, self).__init__(*args, **kwargs)
		
		gener_list = [('', '----')]
		for e in Style.objects.all():
			gener_list.append ((e.id, e.gener))

		state_list = [('', '----')]
		for e in State.objects.all():
			state_list.append((e.id, e.name))

		city_list = [('', '----')]
		for e in City.objects.all():
			city_list.append((e.id, e.name))

		self.fields['gener'].choices = gener_list
		self.fields['state'].choices = state_list
		self.fields['city'].choices = city_list

class ClubForm (forms.Form):

	name = forms.CharField(label='Nome')
	owner = forms.CharField(label='Responsável')
	opened = forms.CharField(label='Funcionamento')

	state = forms.ChoiceField(label='Estado')
	city = forms.ChoiceField(label='Cidade')
	neighborhood = forms.CharField(label='Bairro')
	address = forms.CharField(label='Endereço')

	contact = forms.CharField(label='Contato')

	def __init__(self, *args, **kwargs):
		super(ClubForm, self).__init__(*args, **kwargs)
		
		state_list = [('', '----')]
		for e in State.objects.all():
			state_list.append((e.id, e.name))

		city_list = [('', '----')]
		for e in City.objects.all():
			city_list.append((e.id, e.name))

		self.fields['state'].choices = state_list
		self.fields['city'].choices = city_list