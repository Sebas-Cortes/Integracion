from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView,registro,eliminar_pres,eliminar_medicamento,listar_pres, agregar_medicamento, login,menu_medico, medicamento, prescripcion, prescripcion_crear,ver_pres,edit_pres, menu_farmacia, ver_meds, presc_farm
from django.contrib.auth.decorators import login_required




urlpatterns = [
    path('', CustomLoginView.as_view(), name="login"),
    path('menu_medico',login_required(menu_medico), name="menu_medico"),
    path('medicamento', login_required(medicamento), name="medicamento"),
    path('prescripcion_crear', login_required(prescripcion_crear), name="prescripcion_crear"),
    path('edit_pres', login_required(edit_pres), name="edit_pres"),
    path('logout/', login_required(LogoutView.as_view(template_name='catalog/login.html')), name='logout'),
    path('menu_farmacia', login_required(menu_farmacia), name='menu_farmacia'),
    path('ver_pres',  login_required(listar_pres), name='ver_pres'),
    path('presc_farm', login_required(presc_farm), name='presc_farm'),
    path('prescripcion<int:id>', login_required(prescripcion), name='prescripcion'),
    path('eliminar_medicamento<int:codigo>',login_required(eliminar_medicamento),name="eliminar_medicamento"),
    path('agregar_medicamento<int:id>', login_required(agregar_medicamento), name='agregar_medicamento'),
    path('registro', login_required(registro), name='registro'),
    path('eliminar_pres<int:id>',login_required(eliminar_pres),name="eliminar_pres")
]