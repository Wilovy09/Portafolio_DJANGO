from django.db import models

class Contacto(models.Model):
    Nombre = models.CharField(max_length=255)
    Correo = models.EmailField()
    Mensaje = models.TextField()

    def __str__(self):
        return self.Nombre
