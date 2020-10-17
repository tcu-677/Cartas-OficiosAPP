from django.urls import path
from django.conf.urls import url
from .views import (
    home,
    OficiosListView,
    OficioCreateView,
    OficioUpdateView,
    OficioDeleteView,
    download_file
    )

urlpatterns = [
    path('', home, name='oficios-home'),
    path('oficios', OficiosListView.as_view(), name='oficios'),
    path('oficios/<int:pk>/editar',OficioUpdateView.as_view(), name='oficio-update'),
    path('oficios/<int:pk>/eliminar', OficioDeleteView.as_view(), name='oficio-delete'),
    path('oficios/nuevo',OficioCreateView.as_view(), name='oficio-create'),
    path('oficios/<str:path>/descargar/',download_file,name='oficio-download')
]
