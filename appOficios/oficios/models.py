from django.db import models
from django.db.models import Index
from django.urls import reverse


# Create your models here.

class Oficio(models.Model):
    fecha_de_creacion = models.DateTimeField(auto_now_add=True ,verbose_name='Fecha de creación')
    codigo_de_oficio = models.CharField(verbose_name='Código de oficio' , max_length=500)
    unidad_academica = models.CharField(verbose_name='Unidad académica' , max_length=500)
    a_quien_se_dirige = models.CharField(verbose_name='Dirigido a' , max_length=500)
    asunto = models.TextField(verbose_name='Asunto')
    oficio = models.FileField(verbose_name='Oficio')

    # Function to redirect when an elector is successfully created
    def get_absolute_url(self):
        return reverse('oficios')

    class Meta:
        indexes = [Index(fields=['codigo_de_oficio'])]
        ordering = ['-codigo_de_oficio'] 
