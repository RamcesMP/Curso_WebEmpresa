from .models import Link

def ctx_dic(request):
    ctx = {}
    links=Link.objects.all()
    for link in links:
        ctx[link.Key]= link.url 
    return ctx