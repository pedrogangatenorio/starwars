from django.utils.deprecation import MiddlewareMixin
from films.services import filmservice
from starwars.settings import FILMENTITY, PEOPLENTITY
from films.models.film import Film

class CheckEntityMiddleware(MiddlewareMixin):
    def process_request(self, request):     
    	films = Film.objects.all()
    	if not films:
    		filmservice.getEntityModel(FILMENTITY)
    		filmservice.getEntityModel(PEOPLENTITY)

