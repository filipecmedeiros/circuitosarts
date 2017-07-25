from django.contrib import admin

from .models import State, City, Style, Artist, Club

# Register your models here.
class StateAdmin (admin.ModelAdmin):
	list_display = ['name']
	search_fields = ['name']

class CityAdmin (admin.ModelAdmin):
	list_display = ['name', 'state']
	search_fields = ['name']

class StyleAdmin (admin.ModelAdmin):
	list_display = ['gener']
	search_fields = ['gener']	

class ArtistAdmin (admin.ModelAdmin):

	list_display = ['name', 'gener', 'price', 'contact', 'state', 'city', 'neighborhood', 'address', 'created', 'modified']
	search_fields = ['name', 'gener__gener', 'price', 'state__name', 'city__name']
	list_filter = ['created', 'modified']

class ClubAdmin (admin.ModelAdmin):

	list_display = ['name', 'owner', 'opened', 'contact', 'state', 'city', 'neighborhood', 'address', 'created', 'modified']
	search_fields = ['name', 'owner', 'state__name', 'city__name', 'neighborhood']
	list_filter = ['created', 'modified']

admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Club, ClubAdmin)