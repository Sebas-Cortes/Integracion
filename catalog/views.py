from django.shortcuts import render

# Create your views here.

def menu_template(request):
    return render(request, 'catalog/menu_template.html')
def medicamento_template(request):
    return render(request, 'catalog/medicamento_template.html')
def receta_template(request):
    return render(request, 'catalog/receta_template.html')