from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

class Producto(models.Model):
    
    nombre=models.CharField(max_length=50)
    desc=models.CharField(max_length=100, null=False)
    precio = models.IntegerField(null=False)
    imagen=models.ImageField(upload_to='productos',null=True)

    
    def __str__(self):
        return self.nombre #Esto es para que en la página de Django se muestre el nombre del producto
    

class Persona(models.Model):
    
    nombre=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    alias=models.CharField(max_length=50)
    telefono=models.CharField(max_length=12)
    direccion=models.CharField(max_length=100)
    tipo_usuario=models.CharField(max_length=13)
    
    def __str__(self):
        return self.nombre #Esto es para que en la página de Django se muestre el nombre del producto

class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

class ItemCompra(models.Model):
    compra = models.ForeignKey(Compra, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)