from django import forms
from apps.Productos.models import Productos

class ProductoForm(forms.ModelForm):
	class Meta:

		model = Productos

		fields = [

			'nombreProducto',
			'descripcion',
			'costo',
			'disponibilidad',
			'categoria',

		]

		labels = {

			'nombreProducto' : 'Nombre del producto',
			'descripcion' : 'Descripcion del producto',
			'costo' : 'Costo',
			'disponibilidad' : 'Disponibilidad',
			'categoria' : 'Categoria',
		}

		widgets = {

			'nombreProducto':forms.TextInput(attrs={'class' : 'form-control'}),
			'descripcion':forms.TextInput(attrs={'class' : 'form-control'}),
			'costo':forms.TextInput(attrs={'class' : 'form-control'}),
			'disponibilidad':forms.TextInput(attrs={'class' : 'form-control'}),
			'categoria':forms.TextInput(attrs={'class' : 'form-control'}),

		}


