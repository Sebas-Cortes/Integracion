from django.db import models
from django_userforeignkey.models.fields import UserForeignKey

# Create your models here.
class Prescripcion (models.Model):
    idPrescripcion = models.AutoField(primary_key=True, verbose_name="Id prescripcion")
    rutPaciente = models.CharField(max_length=10, blank=False, null=False, verbose_name="Rut del paciente")
    fecha = models.DateField(auto_now_add=True, verbose_name="Fecha de creacion de prescripcion")
    medico = UserForeignKey(auto_user_add=True, verbose_name = "Medico")
class Receta (models.Model):
    idReceta = models.AutoField(primary_key=True, verbose_name="Id de la receta")
    medicamento = models.CharField(max_length=30, blank=False, null=False, verbose_name="Nombre del medicamento")
    cantidad = models.IntegerField(blank=False, null=False, verbose_name="Cantidad del medicamento")
    prescripcion = models.ForeignKey(Prescripcion, on_delete=models.CASCADE)
