from django.shortcuts import render
from api.serializers import PresSerializers, RecetaSerializers
from rest_framework.decorators import api_view, permission_classes
from catalog.models import Prescripcion, Receta
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt

@api_view(['GET'])
def pres(request,rut):
    if request.method == 'GET':
        pres = Prescripcion.objects.get(rutPaciente=rut)
        res = Receta.objects.filter(prescripcion=pres)
        serializer = RecetaSerializers(res, many=True)
        return Response(serializer.data)