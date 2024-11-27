from django.shortcuts import render
from .models import Producto
# Create your views here.
def home(request):
    return render (request, 'home.html')

def producto(request):
    productos=Producto.objects.all()
    return render (request, 'producto.html',{'productos':productos})

def carrito(request):
    return render(request,'carrito.html')