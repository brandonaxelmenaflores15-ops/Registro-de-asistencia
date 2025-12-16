from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar/', views.agregar_alumno, name='agregar'),
    path('asistencia/', views.pasar_lista, name='asistencia'),
    path('eliminar/<int:alumno_id>/', views.eliminar_alumno, name='eliminar'),
]
