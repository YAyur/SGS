from uuid import uuid4
from django.db import models


class Recurso(models.Model):

    nombre = models.CharField(max_length=200)
    Descripcion = models.TextField()

    class Meta:
        verbose_name = "Recurso"
        verbose_name_plural = "Recursos"

    def __str__(self):
        return self.nombre
