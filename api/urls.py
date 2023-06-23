from django.urls import path
from api.views import pres

urlpatterns = [
    path('pres/<str:rut>', pres, name="pres")
]