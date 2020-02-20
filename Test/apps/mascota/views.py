from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.mascota.form import MascotaForm
from .models import Mascota
# Create your views here.

def index(request):
    ''' print("_"*100) '''
    lista_mascotas = Mascota.objects.all()
    ''' print(lista_mascotas) '''
    contexto = {'lista_mascotas': lista_mascotas}
    return render(request, 'mascota/index.html', contexto)

def FormMascota(request):
    if(request.method == 'POST'):
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = MascotaForm()

    return render(request, 'mascota/form_ingreso.html', {'form': form})

def EliminarMascota(request, id):
    mascota = Mascota.objects.get(id=id)  
    mascota.delete()  
    return redirect("index")  
