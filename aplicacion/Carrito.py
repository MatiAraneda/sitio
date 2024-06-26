from .models import Producto
from django.contrib.auth.models import User 

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "acumulado": producto.precio,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.precio
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.precio
            if self.carrito[id]["cantidad"] <= 0:
                self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

    def get_items(self):
        productos_en_carrito = []
        for item in self.carrito.values():
            producto = {
                'nombre': item['nombre'],
                'acumulado': item['acumulado'],
                'cantidad': item['cantidad'],
            }
            productos_en_carrito.append(producto)
        return productos_en_carrito

    def get_total_carrito(self):
        total = 0
        for item in self.carrito.values():
            total += item['acumulado']
        return total

    def asociar_compra_a_usuario(self, user):
        # Aquí podrías guardar la compra en la base de datos asociándola al usuario
        # Por simplicidad, aquí simplemente lo mostramos como un ejemplo
        print(f"Compra asociada al usuario: {user.username}")