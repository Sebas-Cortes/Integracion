from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'catalog/login.html')
<<<<<<< Updated upstream

def medicamento_template(request):
    return render(request, 'catalog/medicamento_template.html')

def medicamento(request):
    return render(request, 'catalog/medicamento.html')

def menu_medico(request):
    return render(request, 'catalog/menu_medico.html')

def receta_template(request):
    return render(request, 'catalog/receta_template.html')

def receta(request):
    return render(request, 'catalog/receta.html')
=======
def menu_medico(request):
    return render(request, 'catalog/menu_medico.html')
def medicamento(request):
    return render(request, 'catalog/medicamento.html')
def prescripcion_crear(request):
    return render(request, 'catalog/prescripcion_crear.html')
def ver_pres(request):
    return render(request, 'catalog/ver_pres.html')
>>>>>>> Stashed changes
