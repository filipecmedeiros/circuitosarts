from django.shortcuts import render

from .models import Artist, Style, State, City, Club

from .forms import ArtistForm, ClubForm

# Create your views here.
def index (request):

	if request.method == 'POST':
		artist_form = ArtistForm(request.POST)

		club_form = ClubForm(request.POST)

		if artist_form.is_valid():
			name = artist_form.cleaned_data['name']
			gener = Style.objects.get(id = artist_form.cleaned_data['gener'])
			state = State.objects.get(id = artist_form.cleaned_data['state'])
			city = City.objects.get(id = artist_form.cleaned_data['city'])
			neighborhood = artist_form.cleaned_data['neighborhood']
			address = artist_form.cleaned_data['address']
			price = artist_form.cleaned_data['price']
			contact = artist_form.cleaned_data['contact']

			Artist.objects.create(name = name, 
				gener=gener, 
				state = state,
				city = city,
				neighborhood = neighborhood,
				address = address,
				price=price,
				contact = contact,
				)

		if club_form.is_valid():
			name = club_form.cleaned_data['name']
			owner = club_form.cleaned_data['owner']
			opened = club_form.cleaned_data['opened']
			state = State.objects.get(id = artist_form.cleaned_data['state'])
			city = City.objects.get(id = artist_form.cleaned_data['city'])
			neighborhood = artist_form.cleaned_data['neighborhood']
			address = artist_form.cleaned_data['address']
			contact = artist_form.cleaned_data['contact']

			Club.objects.create(name = name, 
				owner = owner,
				opened = opened, 
				state = state,
				city = city,
				neighborhood = neighborhood,
				address = address,
				contact = contact,
				)			

	else:
		artist_form = ArtistForm()
		club_form = ClubForm()		
	
	context = {
		'artist_form' : artist_form,
		'club_form' : club_form,
	}

	return render (request, 'index.html', context)