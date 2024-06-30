from django import forms
from .models import Producto
from django.contrib.auth.forms import UserCreationForm

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','desc','precio','imagen']
        
class CustomUserCreationForm(UserCreationForm):
    pass     