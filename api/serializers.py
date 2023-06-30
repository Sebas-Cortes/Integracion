from rest_framework import serializers
from catalog.models import Prescripcion, Receta

class RecetaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = ['idReceta', 'medicamento', 'cantidad', 'prescripcion']

class PresSerializers(serializers.ModelSerializer):
    recetas = RecetaSerializers(many = True, read_only = True)
    class Meta:
        model = Prescripcion
        fields = ['idPrescripcion', 'rutPaciente', 'fecha', 'estado', 'recetas']