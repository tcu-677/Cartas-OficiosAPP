from django.urls import path
from .views import (
    home,
    OficiosListView,
    OficioCreateView,
    OficioUpdateView,
    # DELETE
    )

urlpatterns = [
    path('', home, name='oficios-home'),
    path('oficios', OficiosListView.as_view(), name='oficios'),
    path('oficios/<int:pk>/editar',OficioUpdateView.as_view(), name='oficio-update'),
    # path('oficios/<int:pk>/eliminar',OficioUpdateView.as_view(), name='oficio-update'),
    path('oficios/nuevo',OficioCreateView.as_view(), name='oficio-create')
]
