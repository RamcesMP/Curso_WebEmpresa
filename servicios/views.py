from django.shortcuts import render,HttpResponse
from .models import Servicio

# Create your views here.

def servicios(request):
    servicios=Servicio.objects.all()
    data={
        "servicios":servicios,
    }
    return render(request,"servicios/servicios.html",data)