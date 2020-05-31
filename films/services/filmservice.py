# -*- coding: utf-8 -*-
import requests, json
from films.models.film import Film 
from films.models.character import Character
from films.models.characterImage import CharacterImage
from starwars.settings import APIURL, APIKEYRESULTS, FILMENTITY, PEOPLENTITY

def getEntityModel(entity):
	url = APIURL + entity 
	r = requests.get(url)
	entities = r.json()

	for entityTMP in entities[APIKEYRESULTS]:
		tmp = Film.create_from_j(json.loads(json.dumps(entityTMP))) if entity == FILMENTITY else Character.create_from_j(json.loads(json.dumps(entityTMP)))
		if entity == FILMENTITY and not Film.objects.filter(episode = tmp.episode).exists():
			tmp.save()
		elif entity == PEOPLENTITY and not Character.objects.filter(name = tmp.name).exists():
			tmp.save()

def addImages(context):
	context['images'] = CharacterImage.objects.all();
	context['carrusel_size'] = context['images'].order_by('id').values_list('id', flat=True)
	return context;