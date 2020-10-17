from django.apps import AppConfig


class OficiosConfig(AppConfig):
    name = 'oficios'

    def ready(self):
        import oficios.signals
