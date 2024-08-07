from django.urls import path, include
from .views import index, PlayStation,Calificaciones,carrito,carritovacio,compraf,contacto,contactomensaje,dashboard,DashboardJs,\
    EditarProductos,Estadisticas,index2,login,mensaje,mensajecompra,mensajeperfil,nintendo,ofertas,olvido,perfil,perfileditar,Productos,\
        ProductosJs,perfil_cliente,lista_usuarios_compra,productosregistrados,registro,seguimiento,Usuarios,UsuariosJs,Xbox,PublicarProducto, eliminarProducto,elimUsuario

# Esto es para usar imagenes
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('',index,name='index'),
    path('PlayStation/',PlayStation,name='PlayStation'),
    path('Calificaciones/',Calificaciones,name='Calificaciones'),
    path('carrito/',carrito,name='carrito'),
    path('carritovacio/',carritovacio,name='carritovacio'),
    path('compraf/',compraf,name='compraf'),
    path('contacto/',contacto,name='contacto'),
    path('contactomensaje/',contactomensaje,name='contactomensaje'),
    path('dashboard/',dashboard,name='dashboard'),
    path('DashboardJs/',DashboardJs,name='DashboardJs'),
    path('EditarProductos/',EditarProductos,name='EditarProductos'),
    path('Estadisticas/',Estadisticas,name='Estadisticas'),
    path('index2/',index2,name='index2'),
    path('login/',login,name='login'),
    path('mensajev',mensaje,name='mensaje'),
    path('mensajecompra/',mensajecompra,name='mensajecompra'),
    path('mensajeperfil/',mensajeperfil,name='mensajeperfil'),
    path('nintendo/',nintendo,name='nintendo'),
    path('ofertas/',ofertas,name='ofertas'),
    path('olvido/',olvido,name='olvido'),
    path('perfil/',perfil,name='perfil'),
    path('perfileditar/',perfileditar,name='perfileditar'),
    path('Productos/',Productos,name='Productos'),
    path('ProductosJs/<id>/',ProductosJs,name='ProductosJs'),
    path('productosregistrados/',productosregistrados,name='productosregistrados'),
    path('registro/',registro,name='registro'),
    path('seguimiento/',seguimiento,name='seguimiento'),
    path('Usuarios/',Usuarios,name='Usuarios'),
    path('UsuariosJs/<int:id>/', UsuariosJs, name='UsuariosJs'),
    path('Xbox/',Xbox,name='Xbox'),
    path('PublicarProducto/',PublicarProducto,name='PublicarProducto'),
    path('eliminarProducto/<id>/',eliminarProducto,name="eliminarProducto"),
    path('elimUsuario/<id>/',elimUsuario,name='elimUsuario'),
    path('orden_compra/', views.orden_compra, name='orden_compra'),
    path('pagar/', views.pagar, name='pagar'),
    path('detalle_pedido/', views.resumen_pedido, name='detalle_pedido'),
    path('lista_usuarios_compra/', lista_usuarios_compra, name='lista_usuarios_compra'),
    path('perfil_cliente/', perfil_cliente, name='perfil_cliente'),
    path('cambiar-envio/<int:compra_id>/', views.cambiar_estado_envio, name='cambiar_envio'),


]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Esto es para las imágenes