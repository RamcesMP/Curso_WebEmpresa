from django.shortcuts import render,HttpResponse

# Create your views here.

def visitanos(request):
    return render(request,"visitanos/visitanos.html")