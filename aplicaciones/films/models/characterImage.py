from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns
from django.utils.translation import gettext_lazy as _
from starwars.settings import IMAGEFOLDER
import os

class CharacterImage(models.Model):

	nombre = models.CharField(_(u'Nombre'),max_length=50)
	file = models.FileField(_(u'File'), blank=True, null=True)

	class Meta:
		verbose_name =  _(u"File")
		verbose_name_plural = _(u"Files")

	def __str__(self):
		return self.nombre 
	
	def getRouteImage(self):
		return os.path.join( IMAGEFOLDER, str(self.file))