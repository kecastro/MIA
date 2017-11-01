from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


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
