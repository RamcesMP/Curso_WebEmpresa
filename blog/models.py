from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User 

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=100,unique=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo=models.CharField(max_length=100,unique=True)
    contenido=models.TextField()
    publicado=models.DateTimeField(default=now)
    image=models.ImageField(upload_to="Post",blank=True,null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    categoria=models.ManyToManyField(Categoria)

    def __str__(self):
        return self.titulo