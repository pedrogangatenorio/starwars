from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns
from .characterImage import CharacterImage
from django.utils.translation import gettext_lazy as _

class Character(models.Model):
    name = models.CharField(max_length=100)
    imagen = models.ManyToManyField(CharacterImage, verbose_name=_('Imagen'), blank=True, help_text="Select an image for this character")

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('character-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}'.format(self.name)

    @classmethod
    def create_from_j(cls, film): 
        j2m = {'name': 'name'}
        return cls(**{j2m[k]:v for k,v in film.items() if k in j2m})
