from django.urls import path
from . import views

urlpatterns = [
    # Talleres
    path('talleres/', views.lista_talleres, name='lista_talleres'),
    path('talleres/nuevo/', views.crear_taller, name='crear_taller'),
    path('talleres/editar/<int:pk>/', views.editar_taller, name='editar_taller'),
    path('talleres/eliminar/<int:pk>/', views.eliminar_taller, name='eliminar_taller'),

    # Vehiculos
    path('vehiculos/', views.lista_vehiculos, name='lista_vehiculos'),
    path('vehiculos/nuevo/', views.crear_vehiculo, name='crear_vehiculo'),
    path('vehiculos/editar/<int:pk>/', views.editar_vehiculo, name='editar_vehiculo'),
    path('vehiculos/eliminar/<int:pk>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
]
