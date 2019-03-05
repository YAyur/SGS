from django.db import models
from .acontecimiento import Acontecimiento
from .lugar_hecho import LugarHecho
#from datos.models.turista import Turista

class Hecho(models.Model):

    acontecimiento = models.ForeignKey(Acontecimiento, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)
    fecha_acontecimiento = models.DateField()
    fecha_denuncia = models.DateField()
    lugar = models.ForeignKey(LugarHecho, on_delete=models.CASCADE)


    
  

    #denunciado por

    #implicados// aun no 

    class Meta:
        verbose_name = "Hecho"
        verbose_name_plural = "Hechos"

    def __str__(self):
        return self.descripcion
