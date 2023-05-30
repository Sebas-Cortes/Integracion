from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'catalog/login.html')
def menu_medico_template(request):
    return render(request, 'catalog/menu_medico.html')
def medicamento_template(request):
    return render(request, 'catalog/medicamento_template.html')
def receta_template(request):
    return render(request, 'catalog/receta_template.html')