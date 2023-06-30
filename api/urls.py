from django.urls import path
from api.views import pres, putPres, getPres

urlpatterns = [
    path('pres/<str:rut>', pres, name="pres"),
    path('putPres/<str:rut>',putPres, name='putPres'),
    path('getPres/<int:id>', getPres, name='getPres')
]