from django.urls import path
from .views import visitanos

urlpatterns = [
    path('', visitanos , name="visitanos"),
]
