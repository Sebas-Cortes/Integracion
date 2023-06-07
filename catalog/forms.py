from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Prescripcion, Receta

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='',
                                widget=forms.TextInput(attrs={'name': 'user','placeholder':'Nombre de usuario'}))
    password = forms.CharField(label='',
                                widget=forms.PasswordInput(attrs={'name': 'pass','placeholder':'Contraseña'}))
    
class PrescripcionForm(forms.ModelForm):
    class Meta:
        model = Prescripcion
        fields = ['rutPaciente']
        help_texts = {k: "" for k in fields}
        labels = {'rutPaciente' : 'Rut del paciente'}
        widgets = {
            'rutPaciente' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Rut del paciente',
            })
        }

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['medicamento', 'cantidad']
        help_texts = {k: "" for k in fields}
        labels = {
            'medicamento' : 'Nombre del medicamento',
            'cantidad' : 'Cantidad del medicamento'
        }
        widgets = {
            'medicamento' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Medicamento',
            }),
            'cantidad' : forms.NumberInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Cantidad',
            })
        }