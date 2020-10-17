from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime

from .models import Oficio


# Will be execute everytime when an elector is created
@receiver(post_save, sender=Oficio)
def update_statistics_create(sender, instance, created, **kwargs):
    if created:
        last_inserted_element_id = instance.id
        code = str(last_inserted_element_id)

        if len(code) == 1:
            code = '00' + code
        
        elif len(code) == 2:
            code = '0' + code

        new_code = f'OdD-{code}-{datetime.now().year}'
        instance.codigo_de_oficio = new_code
        instance.save()