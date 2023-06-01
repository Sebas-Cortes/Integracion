from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import LoginForm
# Create your views here.

def login(request):
    return render(request, 'catalog/login.html')
def menu_medico(request):
    return render(request, 'catalog/menu_medico.html')
def medicamento(request):
    return render(request, 'catalog/medicamento.html')
def prescripcion_crear(request):
    return render(request, 'catalog/prescripcion_crear.html')
def ver_pres(request):
    return render(request, 'catalog/ver_pres.html')
def edit_pres(request):
    return render(request, 'catalog/edit_pres.html')

class CustomLoginView(LoginView):
    template_name = "catalog/login.html"
    form_class = LoginForm

