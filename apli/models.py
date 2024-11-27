from django.db import models

# Create your models here.
class Animal(models.Model):
    id = models.AutoField(primary_key=True)  # Clave primaria automática
    nombre = models.CharField(max_length=100, verbose_name="Nombre del animal")
    especie = models.CharField(max_length=100, verbose_name="Especie del animal")
    habitat = models.CharField(max_length=100, verbose_name="Hábitat del animal")
    tamaño = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Tamaño (metros)")
    edad = models.PositiveIntegerField(verbose_name="Edad (años)")
    alimentacion = models.TextField(verbose_name="Tipo de alimentación")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio ")
    estado_salud = models.CharField(max_length=100, verbose_name="Estado de salud")
    fecha_ingreso = models.DateField(verbose_name="Fecha de ingreso")

    def __str__(self):
        return f"{self.nombre} ({self.especie})"

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animales"
        ordering = ['nombre']  # Ordenar por nombre al listar en el admin

# Modelo para la tabla "Productos"
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