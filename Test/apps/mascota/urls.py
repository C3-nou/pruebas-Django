from django.urls import path
from apps.mascota.views import index, FormMascota, EliminarMascota

urlpatterns = [
    path('',index, name='index'),
    path('newAnimal/', FormMascota, name="mascota_create"),
    path('delete/<int:id>', EliminarMascota, name="destroy")
]