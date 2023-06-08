from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Prescripcion, Receta

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='',
                                widget=forms.TextInput(attrs={'name': 'user','placeholder':'Nombre de usuario'}))
    password = forms.CharField(label='',
                                widget=forms.PasswordInput(attrs={'name': 'pass','placeholder':'Contraseña'}))
    
class UserForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'class': 'form-control bg-dark text-white','placeholder':'Contraseña','id':'reg-pass'}))
    password2 = forms.CharField(label='Confirmas contraseña',widget=forms.PasswordInput(attrs={'class': 'form-control bg-dark text-white','placeholder':'Contraseña','id':'reg-pass2'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-white',
                'placeholder': 'Nombre de usuario',
                'id': 'reg-usu'}),
            'email': forms.EmailInput(attrs={
                'class': 'form-control bg-dark text-white',
                'placeholder': 'Correo electrónico',
                'id': 'reg-email'})
        }
    
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