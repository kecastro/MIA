from django.conf.urls import url

from . import views

app_name = "mia"
urlpatterns = [
    url(r"^$", views.signin, name="login"),
    url(r"^home/$", views.home, name="index"),
    url(r"^agregarpersona/$", views.registerPatient, name="registerPatient"),
    url(r'^getallpatients/(?P<query>[\w\-]+)$', views.getAllPatients , name='patientsSearch'),
    url(r'^persona/$', views.editPatient, name='editPatient'),

]