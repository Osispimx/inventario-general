from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def tablaCate(request):  
    return render(request, 'listaCategorias.html')
    