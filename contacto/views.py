from django.shortcuts import render,HttpResponse, redirect ,reverse
from .forms import *
# Create your views here.

def contacto(request):
    form=ContactForm()
    if request.method == "POST":
        form=ContactForm(data=request.POST)
        if form.is_valid():
            name=request.POST.get("name","")
            email=request.POST.get("name","")
            content=request.POST.get("name","")
            return redirect(reverse('contacto'))
    data={
        "form":form,
    }
    return render(request,"contacto/contacto.html",data)