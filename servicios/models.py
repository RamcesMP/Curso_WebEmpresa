from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo=models.CharField(max_length=100,unique=True)
    subtitulo=models.CharField(max_length=100,unique=True)
    contenido=models.TextField()
    image=models.ImageField(upload_to='servicios',blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Servicio'
        verbose_name_plural='Servicios'
        ordering=['-created']
    def __str__(self):
        return self.titulo