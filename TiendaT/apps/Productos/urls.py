from django.urls import path
from apps.Productos.views import index, invproductos, invcategorias, viewProductos, viewCategoria, viewVenta, nuevoRegistro, editarRegistro, eliminarRegistro, nuevoRegistroc, editarRegistroc, eliminarRegistroc, ventas
app_name = 'Productos';
urlpatterns = [
	path('', index),
	path('index', index),
	path('invproductos', viewProductos.as_view(), name="listaProductos"),
	path('invcategorias', viewCategoria.as_view(), name="listaCategorias"),
	path('nuevoRegistro', nuevoRegistro, name="nuevoRegistro"),
	path('editarRegistro/<id>', editarRegistro, name="editarRegistro"),
	path('eliminarRegistro/<id>', eliminarRegistro, name="eliminarRegistro"),
	path('nuevoRegistroc', nuevoRegistroc, name="nuevoRegistroc"),
	path('editarRegistroc/<id>', editarRegistroc, name="editarRegistroc"),
 	path('eliminarRegistroc/<id>', eliminarRegistroc, name="eliminarRegistroc"),
 	path('ventas', viewVenta.as_view()),
]