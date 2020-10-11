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
        print('Pase')
        response = super().form_valid(form)
        messages.success(self.request, "Oficio agregado satisfactoriamente")
        return response

class UpdateOficioView(LoginRequiredMixin, UpdateView):
    model = Oficio
    fields = [
        'codigo_de_oficio',
        'unidad_academica',
        'a_quien_se_dirige',
        'asunto',
        'oficio'
    ]
    template_name_suffix = '_update_form'
