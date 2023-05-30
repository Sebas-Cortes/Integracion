from django.urls import path
from .views import login,menu_medico, medicamento, receta_template, receta, medicamento_template


urlpatterns = [
    path('', login, name="login"),
    path('menu_medico', menu_medico, name="menu_medico"),
    path('medicamento_template', medicamento_template, name="medicamento_template"),    
    path('medicamento', medicamento, name="medicamento"),
    path('menu_medico', receta_template, name="menu_medico"),
    path('receta_template', receta_template, name="receta_template"),
    path('receta', receta, name="receta"),    
]