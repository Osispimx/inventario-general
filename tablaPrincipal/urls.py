from django.urls import path
from tablaPrincipal import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('principalTel/',views.lista_equipo,name='principalTel'),
    path('agregarTel/',views.crear_equipo,name='agregarTel'),
    path('modifTab/<int:pk>/editar/',views.editar_equipo,name='editarTel'),
    path('detalles/<int:pk>', views.detalles, name='detallesTel'),
]
