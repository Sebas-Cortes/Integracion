from django.urls import path
from . import views
from .views import menu_template, medicamento_template, receta_template


urlpatterns = [
    path('', menu_template, name="menu_template"),
    path('medicamento_template', medicamento_template, name="medicamento_template"),
    path('receta_template', receta_template, name="receta_template"),
]