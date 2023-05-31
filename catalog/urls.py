from django.urls import path
<<<<<<< Updated upstream
from .views import login,menu_medico, medicamento, receta_template, receta, medicamento_template
=======
from . import views
from .views import login,menu_medico, medicamento, prescripcion_crear,ver_pres
>>>>>>> Stashed changes


urlpatterns = [
    path('', login, name="login"),
    path('menu_medico', menu_medico, name="menu_medico"),
<<<<<<< Updated upstream
    path('medicamento_template', medicamento_template, name="medicamento_template"),    
    path('medicamento', medicamento, name="medicamento"),
    path('menu_medico', receta_template, name="menu_medico"),
    path('receta_template', receta_template, name="receta_template"),
    path('receta', receta, name="receta"),    
=======
    path('medicamento', medicamento, name="medicamento"),
    path('prescripcion_crear', prescripcion_crear, name="prescripcion_crear"),
    path('ver_pres', ver_pres, name="ver_pres"),
>>>>>>> Stashed changes
]