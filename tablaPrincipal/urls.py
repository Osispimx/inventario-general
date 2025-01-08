from django.urls import path
from . import views

urlpatterns = [
    path('principal/',views.lista_equipo,name='principal'),
    path('agregar/',views.crear_equipo,name='agregar'),
    path('inventario/<int:pk>/editar/',views.editar_equipo,name='editar'),
    path('inventario/<int:pk>/eliminar/',views.eliminar_equipo,name='eliminar'),
    path('generate_qr/<int:pk>', views.generate_qr, name='generate_qr'),
    path('qr_page/<int:pk>', views.qr_page, name='qr_page'),
    path('detalles/<int:pk>', views.detalles, name='detalles')
]
