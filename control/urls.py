from django.urls import path
from control import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('modifTab/<str:app_name>/<str:model_name>/<int:pk>/eliminar/',views.eliminar_equipo,name='eliminar'),
    path('generate_qr/<str:app_name>/<str:model_name>/<int:pk>', views.generate_qr, name='generate_qr'),
    path('qr_page/<str:app_name>/<str:model_name>/<int:pk>', views.qr_page, name='qr_page'),
]