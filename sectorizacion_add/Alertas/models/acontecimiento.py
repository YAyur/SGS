from django.db import models

class Acontecimiento(models.Model):

    nombre= models.CharField(max_length=30)
    descripcion = models.TextField()

    class Meta:
        verbose_name = "Acontecimiento"
        verbose_name_plural = "Acontecimientos"

    def __str__(self):
        return self.nombre
