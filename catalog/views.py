from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView

from catalog.models import Prescripcion, Receta
from .forms import LoginForm, PrescripcionForm, RecetaForm
from django.contrib import messages
# Create your views here.

def login(request):
    return render(request, 'catalog/login.html')
def menu_medico(request):
    return render(request, 'catalog/menu_medico.html')
def medicamento(request):
    return render(request, 'catalog/medicamento.html')

def prescripcion_crear(request):
    if request.method == 'POST':
        form = PrescripcionForm(request.POST)
        if form.is_valid():
            form.save()
            rut = form.cleaned_data['rutPaciente']
            id = form.instance.idPrescripcion
            messages.success(request, f'Prescripcion para el rut: {rut} creada con exito')
            return redirect('prescripcion', id=id)
    else:
        form = PrescripcionForm()
    
    contexto = { 'form' : form }

    return render(request, 'catalog/prescripcion_crear.html', contexto)

def ver_pres(request):
    return render(request, 'catalog/ver_pres.html')
def edit_pres(request):
    return render(request, 'catalog/edit_pres.html')
def menu_farmacia(request):
    return render(request, 'catalog/menu_farmacia.html')
def ver_meds(request):
    return render(request, 'catalog/ver_meds.html')
def presc_farm(request):
    return render(request, 'catalog/presc_farm.html')

class CustomLoginView(LoginView):
    template_name = "catalog/login.html"
    form_class = LoginForm

def prescripcion(request, id):
    prescripcion = Prescripcion.objects.get(pk=id)
    receta = Receta.objects.filter(prescripcion=prescripcion)
    data = {
        'prescripcion' : prescripcion,
        'lista' : receta,
        }

    return render(request, 'catalog/prescripcion.html', data)

def agregar_medicamento(request, id):
    pres = Prescripcion.objects.get(pk=id)
    if request.method == 'POST':
        form = RecetaForm(request.POST)
        if form.is_valid():
            save = form.save(commit=False)
            save.prescripcion = pres
            save.save()
            med = form.cleaned_data['medicamento']
            messages.success(request, f'Medicamento {med} agregado con exito')
            return redirect('prescripcion', id=id)
    else:
        form = RecetaForm()

    contexto = {'form' : form,
                'prescripcion' : pres,}

    return render(request, 'catalog/agregar_medicamento.html', contexto)
