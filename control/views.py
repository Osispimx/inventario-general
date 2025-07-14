from django.apps import apps
from django.shortcuts import render
import qrcode
from django.http import HttpResponse
from io import BytesIO
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def eliminar_equipo(request, app_name,model_name, pk):
    modelo=apps.get_model(app_name,model_name)
    equipo = get_object_or_404(modelo, pk=pk)
    if request.method == "POST":
        equipo.delete()
        return redirect(f'{app_name}:principalObjs')
    return render(request, 'eliminar.html', {'app_name': app_name,'equipo': equipo})
def verificar_equipo(request, pk):
    pass

#vista para generar el código qr
def generate_qr(request, app_name,model_name,pk):
    modelo=apps.get_model(app_name,model_name)
    equipo = get_object_or_404(modelo, pk=pk)
    # El contenido que quieres codificar en el QR
    data = f"https://inventario-general.onrender.com/{app_name}/detalles/{pk}/"

    
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
def qr_page(request, app_name,model_name,pk):
    modelo=apps.get_model(app_name,model_name)
    equipo = get_object_or_404(modelo, pk=pk)
    return render(request, 'qr_page.html',{'app_name': app_name,
        'model_name': model_name,
        'pk': pk,'equipo': equipo})

