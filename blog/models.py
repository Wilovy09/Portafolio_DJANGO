from django.db import models
import datetime

class post(models.Model):
    Imagen = models.ImageField(upload_to='blog/images')
    Titulo = models.CharField(max_length=300)
    Contenido = models.TextField()
    Fecha = models.DateField(datetime.date.today)
    Autor = models.CharField(max_length=300)

    def __str__(self):
        return self.Titulo