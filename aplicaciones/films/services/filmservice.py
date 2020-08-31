# -*- coding: utf-8 -*-
import requests, json
from ..models.film import Film 
from ..models.character import Character
from starwars.settings import APIURL, APIKEYRESULTS, FILMENTITY, PEOPLENTITY

class EntitiesByAPI:

    def __init__(self, entity):
        self.entity = entity
    
    def getInfo(self):
        url = APIURL + self.entity;
        r = requests.get(url);
        entities = r.json();

        for entityTMP in entities[APIKEYRESULTS]:
            tmp = Film.create_from_j(json.loads(json.dumps(entityTMP))) if self.entity == FILMENTITY else Character.create_from_j(json.loads(json.dumps(entityTMP)))
            if self.entity == FILMENTITY and not Film.objects.filter(episode = tmp.episode).exists():
                tmp.save();
            elif self.entity == PEOPLENTITY and not Character.objects.filter(name = tmp.name).exists():
                tmp.save();

