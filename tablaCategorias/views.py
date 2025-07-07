from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tablaPrincipal.models import inventarioTel
from django.utils import timezone

@login_required
def tablaCate(request):  
    dato = inventarioTel.objects.last()
    fechaTel = dato.fecha.strftime('%Y-%m-%d') if dato and dato.fecha else "Sin fecha"
    return render(request, 'listaCategorias.html',{'fechaTel':fechaTel})
    