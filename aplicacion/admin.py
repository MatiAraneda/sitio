from django.contrib import admin
from .models import Producto, Persona
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','desc','precio','imagen'] #Muestra los datos que se mostrarán desde la página de Django
    list_editable = ['desc','precio','imagen'] #Selecciona los campos que se pueden editar desde la página de Django
    search_field = ['nombre'] #Permite buscar dependiendo del campo ingresado, en este caso, por Nombre
    #list_filter es para filtrar por campo
    list_per_page = 10 #Es decir, solo mostrará 10 productos por página (Django)

class PersonaAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellidos','alias','telefono','direccion','tipo_usuario']
    list_editable = ['apellidos','alias','telefono','direccion','tipo_usuario']
    search_field = ['nombre']
    #list_filter es para filtrar por campo
    list_per_page = 10 


admin.site.register(Producto, ProductoAdmin) #Esto se vincula con models.py, la extensión ProductoAdmin hace referencia a la clase creada arriba
admin.site.register(Persona, PersonaAdmin)