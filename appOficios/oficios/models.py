from django.db import models
from django.db.models import Index
from django.urls import reverse
from datetime import datetime


# Create your models here.

class Oficio(models.Model):
    fecha_de_creacion = models.DateTimeField(auto_now_add=True ,verbose_name='Fecha de creación')
    codigo_de_oficio = models.CharField(verbose_name='Código de oficio' , max_length=500 , unique=True)
    unidad_academica = models.CharField(verbose_name='Unidad académica' , max_length=500)
    a_quien_se_dirige = models.CharField(verbose_name='Dirigido a' , max_length=500)
    asunto = models.TextField(verbose_name='Asunto')
    oficio = models.FileField(verbose_name='Oficio')

    # Function to redirect when an elector is successfully created
    def get_absolute_url(self):
        return reverse('oficios')

    # Function to save the code
    def save(self, *args, **kwargs):
        
        last_inserted_element_id = Oficio.objects.first().id + 1
        code = str(last_inserted_element_id)

        if len(code) == 1:
            code = '00' + code
        
        if len(code) == 2:
            code = '0' + code

        new_code = f'OdD-{code}-{datetime.now().year}'
        self.codigo_de_oficio = new_code
        
        # super().save(*args, **kwargs)

    class Meta:
        indexes = [Index(fields=['codigo_de_oficio'])]
        ordering = ['-codigo_de_oficio'] 
