from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=80, null=False)
    documentId = models.CharField(max_length=20, null=False)
    age = models.IntegerField(null=False)
    photo = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=False)
    map = models.CharField(max_length=50, null=True)

    def __str__(self):
        return "Nombre: " + str(self.name) + " Edad: " + str(self.age)


class Questions(models.Model):
    numberRooms = models.IntegerField(null=False)
    livesWith = models.IntegerField(null=False)
    runningWater = models.BooleanField(default=False, null=False)
    electricity = models.BooleanField(default=False, null=False)
    pets = models.BooleanField(default=False, null=False)
    petsExtra = models.CharField(max_length=20, null=True)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return "Preguntas paciente: " + str(self.patient.name) + " Documento: " + str(self.patient.documentId)