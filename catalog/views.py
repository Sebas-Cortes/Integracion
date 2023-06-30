from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView

from catalog.models import Prescripcion, Receta
from .forms import LoginForm, PrescripcionForm, RecetaForm, UserForm
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
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
            rut = form.cleaned_data['rutPaciente']
            try:
                Prescripcion.objects.get(rutPaciente = rut, estado = True)
                messages.error(request, f'Ya existe una prescripcion para el rut: {rut}')
                return redirect('prescripcion_crear')
            except Prescripcion.DoesNotExist:
                form.save()
                messages.success(request, f'Prescripcion para el rut: {rut} creada con exito')
                return redirect('prescripcion', id=form.instance.idPrecripcion)
                    
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

def listar(request):
    receta= Receta.objects.all()
    data ={
        'receta':receta
    }
    return render (request,'catalog/ver_pres.html',data)

def eliminar_medicamento(request,codigo):
    
    medicamento = Receta.objects.get(pk=codigo)
    pres=medicamento.prescripcion
    medicamento.delete()
    return redirect ('prescripcion',id=pres.idPrescripcion)
        
def listar_pres(request):
    prescripcion= Prescripcion.objects.all()
    data={
        'prescripcion':prescripcion
    }
    return render (request,'catalog/ver_pres.html',data)

def eliminar_pres(request,id):
    
    pres = Prescripcion.objects.get(pk=id)
    pres.delete()

    return redirect ('ver_pres')

@staff_member_required
def registro(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            nick1 = form.cleaned_data['username']
            messages.success(request, f'Usuario {nick1} creado con exito')
            return redirect('menu_medico')
    else:
        form = UserForm()

    contexto = { 'form' : form }

    return render(request,'catalog/registro.html', contexto)