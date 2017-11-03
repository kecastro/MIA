from django import forms
from models import *
from django.core.validators import RegexValidator

class PatientForm(forms.ModelForm):

    name = forms.CharField(label="Nombre", max_length=80, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    documentId = forms.CharField(label="Documento", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    age = forms.IntegerField(label="Edad", max_value=200, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    photo = forms.CharField(label="Foto", max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'opcional'}), required=False)
    address = forms.CharField(label="Direccion", max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    map = forms.CharField(label="Ubicacion mapa", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'opcional'}), required=False)

    class Meta:
        model = Patient
        fields = ['name', 'documentId', 'age', 'photo', 'address', 'map']


class QuestionsForm(forms.ModelForm):

    PETS = (
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
        ('Aves', 'Aves'),
        ('Otro', 'Otro'),
    )

    TRUE_FALSE_CHOICES = (
        (True, 'Si'),
        (False, 'No')
    )

    numberRooms = forms.IntegerField(label="Numero de cuartos", widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    livesWith = forms.IntegerField(label="Vive con", widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    runningWater = forms.ChoiceField(label="Agua potable", choices=TRUE_FALSE_CHOICES,
                                      widget=forms.Select(attrs={'class': 'selectpicker show-tick form-control'}))
    electricity = forms.ChoiceField(label="Electricidad", choices=TRUE_FALSE_CHOICES,
                                      widget=forms.Select(attrs={'class': 'selectpicker show-tick form-control'}))
    pets = forms.ChoiceField(label="Mascotas", choices=TRUE_FALSE_CHOICES,
                                      widget=forms.Select(attrs={'class': 'selectpicker show-tick form-control'}))
    petsExtra = forms.ChoiceField(label="Que mascota", choices=PETS,
                             widget=forms.Select(attrs={'class': 'selectpicker show-tick form-control'}), required=False)

    class Meta:
        model = Questions
        fields = ['numberRooms', 'livesWith', 'runningWater', 'electricity', 'pets', 'petsExtra']

