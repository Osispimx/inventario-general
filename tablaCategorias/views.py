from django.shortcuts import render
from .models import models
from django.contrib.auth.decorators import login_required

@login_required
def tablaCate():
    cate=inventario.objects.all().order_by('id')
        
    
def crearCate():
    pass