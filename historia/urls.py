from django.urls import path
from .views import historia

urlpatterns = [
    path('', historia , name="historia"),
]
