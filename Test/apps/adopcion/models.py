from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    domicilo = models.TextField()

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)