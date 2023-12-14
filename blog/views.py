from django.shortcuts import render,HttpResponse
from .models import Categoria,Post
# Create your views here.

def blog(request):
    posts=Post.objects.all()
    categorias=Categoria.objects.all()
    data={
        "posts":posts,
        "categorias":categorias,
    }
    return render(request,"blog/blog.html",data)

def categoria(request,categoria_id):
    posts=Post.objects.filter(id=categoria_id)
    categorias=Categoria.objects.all()
    data={
        "posts":posts,
        "categorias":categorias,
    }
    return render(request,"blog/blog.html",data)