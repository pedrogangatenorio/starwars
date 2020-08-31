from django.db import models
from django.contrib.auth.models import User

class Like(models.Model):
    usuario = models.ForeignKey(User, verbose_name=('Usuario'), on_delete=models.PROTECT, blank = False, null = False)
    fecha = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'

    def __str__(self):
        return '{0} - {1}'.format( self.usuario, self.fecha)
