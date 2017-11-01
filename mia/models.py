from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=80, null=False)
    documentId = models.CharField(max_length=20, null=False)
    age = models.IntegerField(max_length=3, null=False)
    photo = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=False)
    map = models.CharField(max_length=50, null=True)

    def __str__(self):
        return "Nombre: " + str(self.name) + " Edad: " + str(self.age)


class Questions(models.Model):
    numberRooms = models.IntegerField()
    livesWith = models.IntegerField()
    runningWater = models.BooleanField(default=False)
    electricity = models.BooleanField(default=False)
    pets = models.BooleanField(default=False)
    petsExtra = models.CharField(max_length=20)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return "Preguntas paciente: " + str(self.patient.name) + " Documento: " + str(self.patient.documentId)