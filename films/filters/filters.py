from films.models.film import Film
import django_filters

class FilmFilter(django_filters.FilterSet):

	class Meta:
		model = Film
		fields = {
		  	'title': ['icontains'],
		  	'producer': ['icontains'],
		  	'director': ['icontains'],
		}
