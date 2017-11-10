# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import *


# Create your views here.


def signin(request):

    if request.user.is_authenticated:
        return redirect("mia:index")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if not request.POST.get("remember", None):
                    request.session.set_expiry(0)
                else:
                    request.session.set_expiry(1209600)
                return redirect("mia:index")
            else:
                return render(request, "mia/login.html", {"error_message": "Cuenta suspendida"})
        else:
            return render(request, "mia/login.html", {"error_message": "Usuario y/o contraseña incorrectos"})
    return render(request, "mia/login.html")

def home(request):
    return render(request, "mia/home.html")

def registerPatient(request):

    context = {}

    formPatient = PatientForm(request.POST or None, prefix='patient')
    formQuestions = QuestionsForm(request.POST or None, prefix='questions')

    if formPatient.is_valid() and formQuestions.is_valid():
        document = formPatient.cleaned_data['documentId']
        if Patient.objects.filter(documentId=document).exists():
            formPatient.add_error("documentId", "La persona con cedula: " + str(document) + " ya existe en el sistema")
        else:
            patient = formPatient.save(commit=False)
            patient.save()
            questions = formQuestions.save(commit=False)
            questions.patient = patient
            questions.save()
            context["message"] = "Persona: " + patient.name + " agregada con exito"

    context["formPatient"] = formPatient
    context["formQuestions"] = formQuestions

    return render(request, 'mia/registerPatient.html', context)

def editPatient(request, pk):

    context = {}
    p = get_object_or_404(Patient, pk=pk)

    formPatient = PatientForm(request.POST or None, prefix='patient', instance=p)
    formQuestions = QuestionsForm(request.POST or None, prefix='questions')

    if formPatient.is_valid():
        p = formPatient.save(commit=False)
        p.save()
        return HttpResponseRedirect(reverse('mia:editPatient', kwargs={'pk': p.id}))

    context["patient"] = p
    context["formPatient"] = formPatient
    context["formQuestions"] = formQuestions

    return render(request, 'mia/patient.html', context)
