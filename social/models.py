from django.db import models

# Create your models here.

class Link(models.Model):
    Key=models.SlugField(verbose_name="nombre clave", max_length=100 , unique=True)
    name=models.CharField(verbose_name="Red Social", max_length=100 )
    url=models.URLField(blank=True,null=True,max_length=100 )
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name