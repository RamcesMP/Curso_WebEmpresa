from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.

def sample(request, politica_id):
    politica=Politica.objects.get(id=politica_id)
    data={
        "politica":politica,
    }
    return render(request,"sample/sample.html",data)


    