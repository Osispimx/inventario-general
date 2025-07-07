import qrcode
import pandas as pd
from django.http import HttpResponse
from io import BytesIO
from django.shortcuts import render, get_object_or_404, redirect
from .models import inventarioTel
from .forms import inventarioform
from django.contrib.auth.decorators import login_required

@login_required
def lista_equipo(request):
    equipo = inventarioTel.objects.all().order_by('id')
    return render(request, 'equiptel.html', {'equipos': equipo})

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
    equipo = get_object_or_404(inventarioTel, pk=pk)
    if request.method == "POST":
        form = inventarioform(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('principalTel')
    else:
        form = inventarioform(instance=equipo)
    return render(request, 'editar.html', {'form': form})
@login_required
def eliminar_equipo(request, pk):
    equipo = get_object_or_404(inventarioTel, pk=pk)
    if request.method == "POST":
        equipo.delete()
        return redirect('principalTel')
    return render(request, 'eliminar.html', {'equipo': equipo})
def verificar_equipo(request, pk):
    pass

#vista para generar el código qr
def generate_qr(request,pk):
    equipo = get_object_or_404(inventarioTel, pk=pk)
    # El contenido que quieres codificar en el QR
    data = f"https://inventario-general.onrender.com/detalles/{equipo.pk}"

    
    data_utf8 = data.encode('utf-8')
    # Generar el código QR
    qr = qrcode.make(data_utf8)

    # Crear un objeto en memoria para la imagen del QR
    img_io = BytesIO()
    qr.save(img_io, 'PNG')  # Guardar la imagen en formato PNG
    img_io.seek(0)

    # Devolver la imagen QR como respuesta HTTP
    return HttpResponse(img_io, content_type='image/png')

#vista para renderizar el qr
def qr_page(request,pk):
    equipo = get_object_or_404(inventarioTel, pk=pk)
    return render(request, 'qr_page.html',{'equipo': equipo})


def detalles(request,pk):
    equipo = get_object_or_404(inventarioTel, pk=pk)
    return render(request, 'verEquipo.html',{'equipo': equipo})