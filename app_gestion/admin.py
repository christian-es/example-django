from django.contrib import admin

# Register your models here.
from app_gestion.models import Pedido, Cliente

admin.site.register(Cliente)
admin.site.register(Pedido)
