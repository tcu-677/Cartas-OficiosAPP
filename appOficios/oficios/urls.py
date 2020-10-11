from django.urls import path
from .views import (
    home,
    OficiosListView,
    OficioCreateView
    )

urlpatterns = [
    path('', home, name='oficios-home'),
    path('oficios', OficiosListView.as_view(), name='oficios'),
    path('oficios/nuevo',OficioCreateView.as_view(), name='oficio-create'),
]
