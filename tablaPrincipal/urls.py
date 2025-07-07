from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('principalTel/',views.lista_equipo,name='principalTel'),
    path('agregar/',views.crear_equipo,name='agregar'),
    path('modifTab/<int:pk>/editar/',views.editar_equipo,name='editar'),
    path('modifTab/<int:pk>/eliminar/',views.eliminar_equipo,name='eliminar'),
    path('generate_qr/<int:pk>', views.generate_qr, name='generate_qr'),
    path('qr_page/<int:pk>', views.qr_page, name='qr_page'),
    path('detalles/<int:pk>', views.detalles, name='detalles'),
]
