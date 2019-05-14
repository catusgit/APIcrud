from django.db import models

class CatalogoModelo(model.Model):
    nombre = models.CharField(max_length = 200)
    detalle = models.CharField(max_length = 200)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre