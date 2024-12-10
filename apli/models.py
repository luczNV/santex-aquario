from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key=True)  # Clave primaria automática
    producto = models.CharField(max_length=150, verbose_name="Nombre del producto")
    descripcion = models.TextField(verbose_name="Descripción del producto", blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio ")
    stock = models.PositiveIntegerField(verbose_name="Cantidad en stock")
    categoria = models.CharField(max_length=20,verbose_name="Categoría")
    fecha_ingreso = models.DateField(verbose_name="Fecha de ingreso")
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.producto

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['producto']
        
    @property
    def imageURL(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return '/media/descarga.png'


class User(AbstractUser):
    first_name = None  # Eliminar el campo
    last_name = None   # Eliminar el campo


    def __str__(self):
        return f"{self.email}"

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)  
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="usuario")
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    total_pedido = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    transaction_id = models.CharField(max_length=100, null=True)
    terminado = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.id_pedido)
    
    @property
    def carrito_total(self):
        items = self.pedidoitem_set.all()
        total = sum([item.total for item in items])
        return total

    @property
    def carrito_items(self):
        items = self.pedidoitem_set.all()
        total = sum([item.quantity for item in items])
        return total
    
class PedidoItem(models.Model):
    id_itempedido = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    fecha_add = models.DateTimeField(auto_now_add=True)
    
    @property
    def total(self):
        total = self.producto.precio * self.quantity
        return total
    
class DireccionEnvio(models.Model):
	usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
	direccion = models.CharField(max_length=200, null=False)
	ciudad = models.CharField(max_length=200, null=False)
	provincia = models.CharField(max_length=200, null=False)
	codigo_postal = models.CharField(max_length=200, null=False)
	fecha_envio = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.direccion