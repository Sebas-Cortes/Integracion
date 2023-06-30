from django.shortcuts import render
from api.serializers import PresSerializers, RecetaSerializers
from rest_framework.decorators import api_view, permission_classes
from catalog.models import Prescripcion, Receta
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
@csrf_exempt

@api_view(['GET'])
def pres(request,rut):
    if request.method == 'GET':
        pres = Prescripcion.objects.get(rutPaciente=rut)
        res = Receta.objects.filter(prescripcion=pres)
        serializer = RecetaSerializers(res, many=True)
        return Response(serializer.data)

@api_view(['PUT'])    
def putPres(request, rut):
    try:
        pres = Prescripcion.objects.get(rutPaciente = rut)
    except Prescripcion.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PresSerializers(pres, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])        
def getPres(request, id):
    if request.method == 'GET':
        pres = Prescripcion.objects.get(pk=id)
        serializer_data = []

        data = PresSerializers(pres, many=False).data
        data['recetas'] = RecetaSerializers(Receta.objects.filter(prescripcion=pres), many = True).data
        serializer_data.append(data)

        return Response(serializer_data)