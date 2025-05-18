from django.shortcuts import render, redirect, get_object_or_404
from .models import Taller, Vehiculo
from .forms import TallerForm, VehiculoForm

# -----------------------
# TALLER
# -----------------------

def lista_talleres(request):
    talleres = Taller.objects.all()
    return render(request, 'carritoapp/lista_talleres.html', {'talleres': talleres})

def crear_taller(request):
    if request.method == 'POST':
        form = TallerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_talleres')
    else:
        form = TallerForm()
    return render(request, 'carritoapp/form_taller.html', {'form': form})

def editar_taller(request, pk):
    taller = get_object_or_404(Taller, pk=pk)
    if request.method == 'POST':
        form = TallerForm(request.POST, request.FILES, instance=taller)
        if form.is_valid():
            form.save()
            return redirect('lista_talleres')
    else:
        form = TallerForm(instance=taller)
    return render(request, 'carritoapp/form_taller.html', {'form': form})

def eliminar_taller(request, pk):
    taller = get_object_or_404(Taller, pk=pk)
    if request.method == 'POST':
        taller.delete()
        return redirect('lista_talleres')
    return render(request, 'carritoapp/confirmar_eliminar.html', {'obj': taller, 'tipo': 'Taller'})

# -----------------------
# VEHICULO
# -----------------------

def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'carritoapp/lista_vehiculos.html', {'vehiculos': vehiculos})

def crear_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_vehiculos')
    else:
        form = VehiculoForm()
    return render(request, 'carritoapp/form_vehiculo.html', {'form': form})

def editar_vehiculo(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, request.FILES, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('lista_vehiculos')
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'carritoapp/form_vehiculo.html', {'form': form})

def eliminar_vehiculo(request, pk):
    vehiculo = get_object_or_404(Vehiculo, pk=pk)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('lista_vehiculos')
    return render(request, 'carritoapp/confirmar_eliminar.html', {'obj': vehiculo, 'tipo': 'Vehículo'})
