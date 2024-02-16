from django.db import models
from django.utils import timezone
# Create your models here.


class Categoría(models.Model):
    nombre = models.CharField(max_length=255)
    creado_en = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=225)
    puntaje = models.FloatField()
    stock = models.IntegerField()
    categoría = models.ForeignKey(Categoría, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
