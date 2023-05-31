from django.urls import path

from . import views
from .views import CustomLoginView, login,menu_medico, medicamento, prescripcion_crear,ver_pres

urlpatterns = [
    path('', CustomLoginView.as_view(), name="login"),
    path('menu_medico', menu_medico, name="menu_medico"),
    path('medicamento', medicamento, name="medicamento"),
    path('prescripcion_crear', prescripcion_crear, name="prescripcion_crear"),
    path('ver_pres', ver_pres, name="ver_pres"),
]