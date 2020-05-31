from films.services import filmservice
from films.models.film import Film
from django.views import generic
from films.filters.filters import FilmFilter

class FilmListView(generic.ListView):
    model = Film

    def get_context_data(self, **kwargs):
    	context = super().get_context_data(**kwargs);
    	context['filter'] = FilmFilter(self.request.GET, queryset=self.get_queryset());
    	return filmservice.addImages(context)

class FilmDetailView(generic.DetailView):
    model = Film

    def get_context_data(self, **kwargs):
    	context = super().get_context_data(**kwargs)
    	return filmservice.addImages(context)