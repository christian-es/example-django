from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from app_gestion.models import Cliente, Pedido


class ClienteListView(ListView):
    model = Cliente
    template_name = 'app_gestion/cliente_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cliente_all'] = Cliente.objects.all()
        context['cliente_enabled'] = Cliente.objects.filter(activo=True)
        return context


class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'foto', 'activo', 'sexo']
    success_url = '/clientes'


class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'foto', 'activo', 'sexo']
    template_name_suffix = '_update_form'
    success_url = '/clientes'


class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = '/clientes'


class PedidoListView(ListView):
    model = Pedido
    template_name = 'app_gestion/pedido_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pedido_all'] = Pedido.objects.all()
        return context
