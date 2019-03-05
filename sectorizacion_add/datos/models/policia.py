from django.db import models
from .persona import Persona
from ..enums import *

class Policia(models.Model):

    polica = models.ForeignKey(Persona, on_delete=models.CASCADE)
    grado = models.IntegerField(choices=GRADO_CHOICES)
    descripcion_funciones = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Policia"
        verbose_name_plural = "Policias"

    def __str__(self):
        return self.descripcion_funciones