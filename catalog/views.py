from django.shortcuts import render

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

