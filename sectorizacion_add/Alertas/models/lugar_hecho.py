from django.db import models
from .localizacion import Localizacion


class LugarHecho(models.Model):

    # ubigeo
    direccion = models.CharField(max_length=100)
    cuadra = models.CharField(max_length=30)
    tipo_via = models.CharField(max_length=30)

    referencia = models.CharField(max_length=30)
    localizacion = models.ForeignKey(Localizacion, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "LugarHecho"
        verbose_name_plural = "LugarHechos"

    def __str__(self):
        return self.tipo_via
