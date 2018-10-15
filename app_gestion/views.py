from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from app_gestion.models import Cliente


class ClienteListView(ListView):
    model = Cliente
    template_name = 'app_gestion/cliente_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cliente_all'] = Cliente.objects.all()
        context['cliente_enabled'] = Cliente.objects.filter(activo=True)
        return context
