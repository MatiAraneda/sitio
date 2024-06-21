from django import froms 
from .models import Producto

class ProductoForm(forms.ModelForm):
    
    id=forms.CharField(max_length=10,
                        error_messages={"required":"Ingrese rut sin puntos y con guión ej.:12345678-9"}, 
                        help_text="Debe ingresar rut")
    class Meta:
        model = Producto
        fields = ['id','nombre','desc','precio','imagen']