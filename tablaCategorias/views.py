from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tablaPrincipal.models import inventarioTel
from tablaComputo.models import equipoPcCom

@login_required
def tablaCate(request):  
    datoTel = inventarioTel.objects.last()
    datoPc= equipoPcCom.objects.last()
    fechaTel = datoTel.fecha.strftime('%Y-%m-%d') if datoTel and datoTel.fecha else "Sin fecha"
    fechaPc = datoPc.fecha.strftime('%Y-%m-%d') if datoPc and datoPc.fecha else "Sin fecha"
    return render(request, 'listaCategorias.html',{'fechaTel':fechaTel,'fechaPc':fechaPc})
