from django.utils.deprecation import MiddlewareMixin
from aplicaciones.films.services import filmservice
from aplicaciones.films.models.film import Film
from aplicaciones.films.models.character import Character
from .settings import FILMENTITY, PEOPLENTITY

class CheckEntityMiddleware(MiddlewareMixin):

    def process_request(self, request):     
        films = Film.objects.all()
        peoples = Character.objects.all()
        
        if not films:
            pfilm = filmservice.EntitiesByAPI(FILMENTITY)
            pfilm.getInfo()

        if not peoples:
            ppeople = filmservice.EntitiesByAPI(PEOPLENTITY)
            ppeople.getInfo()
