from django.db import models
from ..enums import *

class Persona(models.Model):

    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    genero = models.IntegerField(choices=GENERO_CHOICES)

    estado_civil = models.IntegerField(choices=ESTADO_CIVIL_CHOICES)
    # podemos agregar con mapas ojo
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=20)
    correo_electronico = models.EmailField(max_length=30)
    celular = models.CharField(max_length=11)
    
    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return self.nombres
