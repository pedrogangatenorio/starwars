import os
from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns
from .character import Character
from .score import Score
from .comment import Comment
from starwars.settings import IMAGEFOLDER

class Film(models.Model):
    title = models.CharField(max_length=100)
    episode = models.PositiveIntegerField(null=True)
    description = models.CharField(max_length=1000)    
    director= models.CharField(max_length=100)    
    producer = models.CharField(max_length=100)
    release_date = models.CharField(max_length=100)
    character = models.ManyToManyField(Character, blank=True, help_text="Select a character for this film")
    score = models.ManyToManyField(Score, related_name='r_score', blank=True)
    comment = models.ManyToManyField(Comment, related_name='r_comment', blank=True)
    image = models.FileField('Imagen', blank=True, null=True)

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('films:film-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}'.format(self.title)

    @classmethod
    def create_from_j(cls, film): 
        j2m = {'title': 'title', 'episode_id':'episode','opening_crawl': 'description', 'director':'director','producer': 'producer','release_date':'release_date'}
        return cls(**{j2m[k]:v for k,v in film.items() if k in j2m})

    def getPuntuacion(self):
        cont = 0
        ass_scores = self.score.all()
        for scr in ass_scores:
            cont += scr.puntuacion
        return '(' + str(cont / len(ass_scores)) + ')' if len(ass_scores) > 0 else str('')

    def votantes(self):
        return self.score.all().values_list('usuario', flat=True)

    def getRouteImage(self):
        return os.path.join( IMAGEFOLDER, str(self.image)) if self.image else None