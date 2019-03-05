from django.db import models
from .persona import Persona
from ..enums import *

class Turista(models.Model):

    
    turista = models.ForeignKey(Persona, on_delete=models.CASCADE)
    grado_academico = models.IntegerField(choices=GRADO_ACADEMICO_CHOICES)
    descripcion= models.CharField(max_length= 100)
    class Meta:
        verbose_name = "Turista"
        verbose_name_plural = "Turistas"

    def __str__(self):
        return self.descripcion
