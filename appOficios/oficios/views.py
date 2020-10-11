from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.contrib import messages


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
    paginate_by = 8


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
        messages.success(self.request, "Oficio modificado satisfactoriamente")
        return response


# import os
# from django.conf import settings
# from django.http import HttpResponse, Http404

# def download(request, path):
#     file_path = os.path.join(settings.MEDIA_ROOT, path)
#     if os.path.exists(file_path):
#         with open(file_path, 'rb') as fh:
#             response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
#             response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
#             return response
#     raise Http404