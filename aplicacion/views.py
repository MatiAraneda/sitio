from django.shortcuts import render, redirect
from datetime import date
from .models import Producto, Pedido, PedidoProducto, Compra, CompraProducto
from django.shortcuts import get_object_or_404, redirect
from .forms import ProductoForm, CustomUserCreationForm,CustomUserChangeForm
from django.contrib import messages
from os import path, remove
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .Carrito import Carrito
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.decorators import login_required
from collections import defaultdict


# Create your views here.


def index (request): 
    return render(request,'aplicacion/index.html')

def PlayStation (request): 
    return render(request,'aplicacion/PlayStation.html')

def Calificaciones (request): 
    return render(request,'aplicacion/Calificaciones.html')

def carrito (request): 
    return render(request,'aplicacion/carrito.html')

def carritovacio (request): 
    return render(request,'aplicacion/carritovacio.html')

def compraf (request): 
    return render(request,'aplicacion/compraf.html')

def contacto (request): 
    return render(request,'aplicacion/contacto.html')

def contactomensaje (request): 
    return render(request,'aplicacion/contactomensaje.html')


def dashboard (request): 
    return render(request,'aplicacion/dashboard.html')

def DashboardJs (request): 
    return render(request,'aplicacion/DashboardJs.html')


def Estadisticas (request): 
    return render(request,'aplicacion/Estadisticas.html')

def index2 (request): 
    return render(request,'aplicacion/index2.html')

def login (request): 
    return render(request,'registration/login.html')

def mensaje (request): 
    return render(request,'aplicacion/mensaje.html')

def mensajecompra (request): 
    return render(request,'aplicacion/mensajecompra.html')

def mensajeperfil (request): 
    return render(request,'aplicacion/mensajeperfil.html')

def nintendo (request):
    productos = Producto.objects.all() 
    return render(request,'aplicacion/nintendo.html', {'productos':productos})

def ofertas (request): 
    return render(request,'aplicacion/ofertas.html')

def olvido (request): 
    return render(request,'aplicacion/olvido.html')

def perfil (request): 
    return render(request,'aplicacion/perfil.html')

def perfileditar (request): 
    return render(request,'aplicacion/perfileditar.html')

def EditarProductos (request): 
    productos = Producto.objects.all()
    
    data ={
        'productos' : productos
    }

    return render(request,'aplicacion/EditarProductos.html',data) 
    
def Productos (request):
    form = ProductoForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        
        messages.success(request,'Producto agregado exitosamente')
        return redirect(to="EditarProductos")
    datos={
        "form": form
    }
    return render(request, 'aplicacion/Productos.html', datos)


def PublicarProducto (request):
    return render(request,'aplicacion/PublicarProducto.html')

def ProductosJs (request, id):         
    
    producto = get_object_or_404(Producto, id=id)
    
    data = {
        'form': ProductoForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado exitosamente")
            return redirect(to="EditarProductos")
        data["form"] = formulario
    
    return render(request,'aplicacion/ProductosJs.html', data)


def productosregistrados (request): 
    return render(request,'aplicacion/productosregistrados.html')

def registro (request): 
    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()        
            user= authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request)
            messages.success(request, "Registro realizado exitosamente")
            return redirect(to=index)
        data["form"] = formulario
    
    return render(request,'registration/registro.html',data)

def seguimiento (request): 
    return render(request,'aplicacion/seguimiento.html')

def Usuarios(request):
    users = User.objects.all()
    datos = {
        'users': users
    }
    return render(request, 'aplicacion/Usuarios.html', datos)

def UsuariosJs(request, id): 
    user = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario modificado exitosamente")
            return redirect('Usuarios')
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'aplicacion/UsuariosJs.html', {'form': form, 'user': user})    


def Xbox (request): 
    return render(request,'aplicacion/xbox.html')

def eliminarProducto(request,id):
    producto = get_object_or_404(Producto,id=id)
    producto.delete()
    messages.success(request, "Eliminado exitosamente")
    return redirect(to="EditarProductos")

def elimUsuario(request,id):
    user = get_object_or_404(User,id=id)
    user.delete()
    messages.success(request, "Eliminado exitosamente")
    return redirect(to="Usuarios")


def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("nintendo")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("nintendo")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("nintendo")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("nintendo")

@login_required
def orden_compra(request):
    carrito = Carrito(request)
    items = carrito.get_items()
    total_carrito = carrito.get_total_carrito()

    carrito.asociar_compra_a_usuario(request.user)

    context = {
        'items': items,
        'total_carrito': total_carrito,
    }

    return render(request, 'aplicacion/resumen_pedido.html', context)

def pagar(request):

    return render(request, 'aplicacion/pagar.html')

def resumen_pedido(request):
    carrito = Carrito(request)
    items = carrito.get_items()
    total_carrito = carrito.get_total_carrito()

    context = {
        'items': items,
        'total_carrito': total_carrito,
    }

    return render(request, 'aplicacion/detalle_pedido.html', context)

def realizar_compra(request):
    carrito = Carrito(request)
    pedido = carrito.procesar_compra(request.user)
    if pedido:
        messages.success(request, 'Compra realizada exitosamente')
        return redirect('detalle_pedido', pedido_id=pedido.id)
    else:
        messages.error(request, 'No hay productos en el carrito')
    return redirect(to="productos")

def detalle_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id, user=request.user)
    items = pedido.pedidoproducto_set.all()
    detalles = []
    for item in items:
        detalles.append({
            'producto': item.producto,
            'cantidad': item.cantidad,
            'precio': item.precio,
            'total': item.cantidad * item.precio
        })
    return render(request, 'aplicacion/detalle_pedido.html', {'pedido': pedido, 'detalles': detalles})

def lista_pedidos(request):
    pedidos = Pedido.objects.filter(user=request.user)
    return render(request, 'aplicacion/lista_pedidos.html', {'pedidos': pedidos})


def lista_usuarios_compra(request):
    compras = Compra.objects.all()
    return render(request, 'aplicacion/lista_usuarios_compra.html', {'compras': compras})

@login_required
def perfil_cliente(request):
    user = request.user
    compras = Compra.objects.filter(usuario=user).order_by('-fecha_compra')

    # Agrupar compras por año y mes
    compras_por_periodo = defaultdict(list)
    for compra in compras:
        periodo = compra.fecha_compra.strftime('%Y-%m')
        compras_por_periodo[periodo].append(compra)

    context = {
        'user': user,
        'compras': dict(compras_por_periodo)
    }
    return render(request, 'aplicacion/perfil_cliente.html', context)

def cambiar_estado_envio(request, compra_id):
    if not request.user.is_superuser:
        return redirect('index')  # Redirige si no es superadmin

    compra = Compra.objects.get(id=compra_id)

    if request.method == 'POST':
        estado_envio = request.POST.get('estado_envio')
        compra.estado_envio = estado_envio
        compra.save()

    return redirect('lista_usuarios_compra')