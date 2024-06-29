from django.db import models
class Producto(models.Model):
    
    nombre=models.CharField(max_length=50)
    desc=models.CharField(max_length=100, null=False)
    precio = models.IntegerField(null=False)
    imagen=models.ImageField(upload_to='productos',null=True)

    
    def __str__(self):
        return self.nombre #Esto es para que en la página de Django se muestre el nombre del producto
    

    