from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key=True)  # Clave primaria automática
    producto = models.CharField(max_length=150, verbose_name="Nombre del producto")
    descripcion = models.TextField(verbose_name="Descripción del producto", blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio ")
    stock = models.PositiveIntegerField(verbose_name="Cantidad en stock")
    proveedor = models.CharField(max_length=150, verbose_name="Proveedor")
    categoria = models.CharField(max_length=20,verbose_name="Categoría")
    fecha_ingreso = models.DateField(verbose_name="Fecha de ingreso")

    def __str__(self):
        return self.producto

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['producto']  # Ordenar por nombre del producto al listar

class User(AbstractUser):
    first_name = None  # Eliminar el campo
    last_name = None   # Eliminar el campo