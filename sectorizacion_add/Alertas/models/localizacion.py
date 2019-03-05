from django.db import models


class Localizacion(models.Model):

    nombre = models.CharField(max_length=100)
    latitud = models.CharField(max_length=50)
    longitud= models.CharField(max_length=50)

    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Localizacion"
        verbose_name_plural = "Localizacions"

    def __str__(self):
        return self.nombre
        