from django.db import models
from django.contrib.auth.models import User
from .like import Like

class Comment(models.Model):
    usuario = models.ForeignKey(User, verbose_name=('Usuario'), on_delete=models.PROTECT, blank = False, null = False)
    texto = models.CharField(max_length=100, blank=False, null=False)
    fecha = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)
    like = models.ManyToManyField(Like, related_name='r_like', blank=True)
    estado = models.BooleanField('Estado', default=True)

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return '{0} - {1}'.format( self.usuario, self.fecha)

    def getUsuariosLikes(self):
        return self.like.all().values_list('usuario__id', flat=True)