from django.urls import path
from .views import sample

urlpatterns = [
    path('<int:politica_id>/', sample , name="sample"),
    
]
