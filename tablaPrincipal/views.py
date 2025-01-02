from django.shortcuts import render, get_object_or_404, redirect
from .models import inventario
from .forms import inventarioform

def lista_equipo(request):
    equipo = inventario.objects.all().order_by('id')
    return render(request, 'inventario.html', {'equipos': equipo})

def crear_equipo(request):
    if request.method == "POST":
        form = inventarioform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('principal')
    else:
        form = inventarioform()
    return render(request, 'agregarEquipo.html', {'form': form})

def editar_equipo(request, pk):
    equipo = get_object_or_404(inventario, pk=pk)
    if request.method == "POST":
        form = inventarioform(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('principal')
    else:
        form = inventarioform(instance=equipo)
    return render(request, 'editar.html', {'form': form})

def eliminar_equipo(request, pk):
    equipo = get_object_or_404(inventario, pk=pk)
    if request.method == "POST":
        equipo.delete()
        return redirect('principal')
    return render(request, 'eliminar.html', {'equipo': equipo})


