from django.shortcuts import render

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

def EditarProductos (request): 
    return render(request,'aplicacion/EditarProductos.html')

def Estadisticas (request): 
    return render(request,'aplicacion/Estadisticas.html')

def index2 (request): 
    return render(request,'aplicacion/index2.html')

def login (request): 
    return render(request,'aplicacion/login.html')

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

def Productos (request): 
    return render(request,'aplicacion/Productos.html')

def ProductosJs (request): 
    return render(request,'aplicacion/ProductosJs.html')

def productosregistrados (request): 
    return render(request,'aplicacion/productosregistrados.html')

def registro (request): 
    return render(request,'aplicacion/registro.html')

def seguimiento (request): 
    return render(request,'aplicacion/seguimiento.html')

def Usuarios (request): 
    return render(request,'aplicacion/Usuarios.html')

def UsuariosJs (request): 
    return render(request,'aplicacion/UsuariosJs.html')

def Xbox (request): 
    return render(request,'aplicacion/xbox.html')

def base (request):
    return render(request,'aplicacion/base.html')