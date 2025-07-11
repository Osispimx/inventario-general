from django.urls import path
from tablaPrincipal import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('principalEqui/',views.lista_equipo,name='principalEqui'),
    path('agregarEqui/',views.crear_equipo,name='agregarEqui'),
    path('modifTabEqui/<int:pk>/editar/',views.editar_equipo,name='editarEqui'),
    path('modifTabEqui/<int:pk>/eliminar/',views.eliminar_equipo,name='eliminarEqui'),
    path('generate_qrEqui/<int:pk>', views.generate_qr, name='generate_qrEqui'),
    path('qr_pageEqui/<int:pk>', views.qr_page, name='qr_pageEqui'),
    path('detallesEqui/<int:pk>', views.detalles, name='detallesEqui'),
]
