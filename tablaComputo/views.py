from django.shortcuts import render, get_object_or_404, redirect
from .models import equipoPcCom
from .forms import inventarioform
from django.contrib.auth.decorators import login_required

@login_required
def lista_equipo(request):
    equipo = equipoPcCom.objects.all().order_by('id')
    return render(request, 'equipcom.html', {'equipos': equipo})

@login_required
def crear_equipo(request):
    if request.method == "POST":
        form = inventarioform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('principalTel')
    else:
        form = inventarioform()
    return render(request, 'agregarEquipo.html', {'form': form})
@login_required
def editar_equipo(request, pk):
    equipo = get_object_or_404(equipoPcCom, pk=pk)
    if request.method == "POST":
        form = inventarioform(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('principalEqui')
    else:
        form = inventarioform(instance=equipo)
    return render(request, 'editar.html', {'form': form})

def detalles(request,pk):
    equipo = get_object_or_404(equipoPcCom, pk=pk)
    return render(request, 'verEquipo.html',{'equipo': equipo})