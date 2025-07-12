from django.urls import path
from tablaComputo import views
urlpatterns = [
    path('principalEqui/',views.lista_equipo,name='principalEqui'),
    path('agregarEqui/',views.crear_equipo,name='agregarEqui'),
    path('modifTabEqui/<int:pk>/editar/',views.editar_equipo,name='editarEqui'),
    path('detalles/<int:pk>', views.detalles, name='detallesTel'),
]
