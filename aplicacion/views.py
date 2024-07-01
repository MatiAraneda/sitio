from django.shortcuts import render
from datetime import date
from .models import Producto
from django.shortcuts import get_object_or_404, redirect
from .forms import ProductoForm, CustomUserCreationForm,CustomUserChangeForm
from django.contrib import messages
from os import path, remove
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

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
    return render(request,'aplicacion/nintendo.html')

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
 
#def Productos (request):
#    data = {
#        'form': ProductoForm()
#    }
#    
#    if request.method == 'POST':
#        formulario = ProductoForm(data=request.POST, files=request.FILES)
#        if formulario.is_valid():
#            formulario.save
#    return render(request, 'aplicacion/Productos.html', data)

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

