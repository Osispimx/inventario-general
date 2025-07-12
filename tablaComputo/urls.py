from django.urls import path
from tablaComputo import views
app_name = 'tablaComputo'
urlpatterns = [
    path('principalEqui/',views.lista_equipo,name='principalObjs'),
    path('agregarEqui/',views.crear_equipo,name='agregarEqui'),
    path('modifTabEqui/<int:pk>/editar/',views.editar_equipo,name='editarEqui'),
    path('detallesEqui/<int:pk>', views.detalles, name='detallesTel'),
]
