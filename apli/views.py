from django.shortcuts import render ,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse
from .forms import *
from .models import *

# Create your views here.

def producto(request):
    productos=Producto.objects.all()
    return render (request, 'producto.html',{'productos':productos})

def producto_views(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'producto_views.html', {'producto': producto})

# Carritoviews

@login_required
def Carrito(request):
    usuario = request.user
    pedido = Pedido.objects.filter(usuario=usuario, terminado=False).first()

    if not pedido:
        items = []
    else:
        items = pedido.pedidoitem_set.all()

    contexto = {'items': items, 'pedido': pedido}
    return render(request, 'carrito.html', contexto)

@login_required
def global_carrito_cantidad(request):
    usuario = request.user
    pedido = Pedido.objects.filter(usuario=usuario, terminado=False).first()
    cantidad = pedido.carrito_items if pedido else 0
    return JsonResponse({'cantidad': cantidad})

@login_required
def agregar_carrito(request, producto_id):
    usuario = request.user
    producto = Producto.objects.get(id=producto_id)
    cantidad = int(request.GET.get('quantity', 1))  # Cantidad predeterminada: 1

    # Obtener o crear el pedido del usuario
    pedido, created = Pedido.objects.get_or_create(usuario=usuario, terminado=False)

    # Buscar si el producto ya está en el carrito
    pedido_item, created = PedidoItem.objects.get_or_create(
        pedido=pedido,
        producto=producto,
    )

    # Incrementar la cantidad del producto
    pedido_item.quantity += cantidad
    pedido_item.save()

    # Retorna el mensaje y el número de items en el carrito
    return JsonResponse({
        'message': f'Se agregaron {cantidad} unidades de {producto.producto} al carrito.',
        'carrito_items': pedido.carrito_items
    })


@login_required
def bajar_cantidad(request, item_id):
    item = PedidoItem.objects.get(id_itempedido=item_id, pedido__usuario=request.user, pedido__terminado=False)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return JsonResponse({'message': 'Cantidad actualizada', 'carrito_items': item.pedido.carrito_items, 'carrito_total': item.pedido.carrito_total})


@login_required
def aumentar_cantidad(request, item_id):
    item = PedidoItem.objects.get(id_itempedido=item_id, pedido__usuario=request.user, pedido__terminado=False)

    item.quantity += 1
    item.save()

    return JsonResponse({'message': 'Cantidad aumentada', 'carrito_items': item.pedido.carrito_items, 'carrito_total': item.pedido.carrito_total})


@login_required
def eliminar_item(request, item_id):
    item = PedidoItem.objects.get(id_itempedido=item_id, pedido__usuario=request.user, pedido__terminado=False)
    pedido = item.pedido

    item.delete()

    return JsonResponse({'message': 'Producto eliminado', 'carrito_items': pedido.carrito_items, 'carrito_total': pedido.carrito_total})



@login_required
def checkout(request):
    pedido = Pedido.objects.filter(usuario=request.user, terminado=False).first()
    items = pedido.pedidoitem_set.all() if pedido else []

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Guardar la dirección de envío
            direccion_envio = form.save(commit=False)
            direccion_envio.usuario = request.user
            direccion_envio.pedido = pedido
            direccion_envio.save()

            # Marcar el pedido como completado
            pedido.terminado = True
            pedido.total_pedido = pedido.carrito_total
            pedido.save()

            # Redirigir a una página de confirmación o gracias
            return redirect('gracias')
    else:
        form = CheckoutForm()

    context = {
        'form': form,
        'pedido': pedido,
        'items': items,
    }
    return render(request, 'checkout.html', context)


def gracias(request):
    return render(request, 'gracias.html')
#main
def home(request):
    return render (request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('/')