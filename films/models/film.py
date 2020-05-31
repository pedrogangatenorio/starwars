from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns

class Film(models.Model):
    title = models.CharField(max_length=100)
    episode = models.PositiveIntegerField(null=True)
    description = models.CharField(max_length=1000)    
    director= models.CharField(max_length=100)    
    producer = models.CharField(max_length=100)
    release_date = models.CharField(max_length=100)

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('film-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}'.format(self.title)

    @classmethod
    def create_from_j(cls, film): 
        j2m = {'title': 'title', 'episode_id':'episode','opening_crawl': 'description', 'director':'director','producer': 'producer','release_date':'release_date'}
        return cls(**{j2m[k]:v for k,v in film.items() if k in j2m})
