from django.db import models

# Create your models here.

class Politica(models.Model):
    titulo=models.CharField(max_length=100)
    contenido=models.TextField()

    def __str__(self):
        return self.titulo