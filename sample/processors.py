from .models import *

def ctx_p(request):
    politicas=Politica.objects.all()
    data={"politicas":politicas}
    return data