from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

import os
from django.conf import settings
from django.http import HttpResponse, Http404


from django.views.generic import(
    ListView,
    UpdateView,
    CreateView,
    DeleteView
)

from .models import Oficio
# Create your views here.


def home(request):
    template = 'oficios/home.html'
    return render(request, template)


class OficiosListView(LoginRequiredMixin, ListView):
    model = Oficio
    paginate_by = 5


class OficioCreateView(LoginRequiredMixin, CreateView):
    model = Oficio
    fields = [
        'unidad_academica',
        'a_quien_se_dirige',
        'asunto',
        'oficio'
    ]
    template_name_suffix = '_create_form'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Oficio agregado satisfactoriamente")
        return response

class OficioUpdateView(LoginRequiredMixin, UpdateView):
    model = Oficio
    fields = [
        'codigo_de_oficio',
        'unidad_academica',
        'a_quien_se_dirige',
        'asunto',
        'oficio'
    ]
    template_name_suffix = '_update_form'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.info(self.request, "Oficio modificado satisfactoriamente")
        return response



class OficioDeleteView(LoginRequiredMixin, DeleteView):
    model = Oficio
    success_url = reverse_lazy('oficios')

    def delete(self, request, *args, **kwargs):
        messages.info(self.request, "Oficio eliminado satisfactoriamente")
        response = super().delete(request, *args, **kwargs)
        return response


def download_file(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    print(file_path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404