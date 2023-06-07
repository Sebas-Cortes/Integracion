from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, agregar_medicamento, login,menu_medico, medicamento, prescripcion, prescripcion_crear,ver_pres,edit_pres, menu_farmacia, ver_meds, presc_farm

urlpatterns = [
    path('', CustomLoginView.as_view(), name="login"),
    path('menu_medico', menu_medico, name="menu_medico"),
    path('medicamento', medicamento, name="medicamento"),
    path('prescripcion_crear', prescripcion_crear, name="prescripcion_crear"),
    path('ver_pres', ver_pres, name="ver_pres"),
    path('edit_pres', edit_pres, name="edit_pres"),
    path('logout/', LogoutView.as_view(template_name='catalog/login.html'), name='logout'),
    path('menu_farmacia', menu_farmacia, name='menu_farmacia'),
    path('ver_meds', ver_meds, name='ver_meds'),
    path('presc_farm', presc_farm, name='presc_farm'),
    path('prescripcion<int:id>', prescripcion, name='prescripcion'),
    path('agregar_medicamento<int:id>', agregar_medicamento, name='agregar_medicamento')
]