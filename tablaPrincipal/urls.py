from django.urls import path
from tablaPrincipal import views
app_name = 'tablaPrincipal'
urlpatterns = [
    path('principalTel/',views.lista_equipo,name='principalObjs'),
    path('agregarTel/',views.crear_equipo,name='agregarTel'),
    path('modifTab/<int:pk>/editar/',views.editar_equipo,name='editarTel'),
    path('detalles/<int:pk>', views.detalles, name='detalles'),
]
