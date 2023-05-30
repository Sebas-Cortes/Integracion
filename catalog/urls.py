from django.urls import path
from . import views
from .views import login,menu_medico, medicamento_template, receta_template


urlpatterns = [
    path('', login, name="login"),
    path('menu_medico', menu_medico, name="menu_medico"),
    path('medicamento_template', medicamento_template, name="medicamento_template"),
    path('receta_template', receta_template, name="receta_template"),
]