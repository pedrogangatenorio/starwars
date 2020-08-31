from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Score(models.Model):
    usuario = models.ForeignKey(User, verbose_name=('Usuario'), on_delete=models.PROTECT, blank = False, null = False)
    puntuacion = models.PositiveIntegerField(null=False, default=1, validators=[MaxValueValidator(5), MinValueValidator(0)])

    class Meta:
        verbose_name = 'Score'
        verbose_name_plural = 'Scores'

    def __str__(self):
        return '{0} - {1}'.format( self.usuario, self.puntuacion)
