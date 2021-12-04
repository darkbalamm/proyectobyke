from django.urls import path

from app1 import views

urlpatterns = [
    path('',views.inicio, name="inicio"),
    path('piezas',views.piezas, name="piezas"),
    path('comentarios',views.comentarios, name="comentarios"),
    path('estadisticas',views.estadisticas, name="estadisticas"),
]