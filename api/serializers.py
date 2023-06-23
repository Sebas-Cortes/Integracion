from rest_framework import serializers
from catalog.models import Prescripcion, Receta

class PresSerializers(serializers.ModelSerializer):
    class Meta:
        model = Prescripcion
        fields = ['idPrescripcion', 'rutPaciente', 'fecha', 'estado']

class RecetaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = ['idReceta', 'medicamento', 'cantidad', 'prescripcion']