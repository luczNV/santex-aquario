from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Producto)
admin.site.register(User)
admin.site.register(Pedido)
admin.site.register(PedidoItem)
admin.site.register(DireccionEnvio)