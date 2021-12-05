from django.urls import path

from app1 import views

urlpatterns = [
    path('',views.inicio, name="inicio"),  
    path('comentarios',views.comentarios, name="comentarios"),
    path('estadisticas',views.estadisticas, name="estadisticas"),

    path('manubrio',views.manubrio,name="manubrio"),
    path('horquilla',views.horquilla, name="horquilla"),
    path('man',views.man, name="man"),
    path('puños',views.puños, name="puños"),
    path('poder',views.poder, name="poder"),

    path('cuadros',views.cuadros,name="cuadros"),
    path('tsup',views.tsup,name="tsup"),
    path('tinf',views.tinf,name="tinf"),
    path('tsillin',views.tsillin,name="tsillin"),
    path('plato',views.plato,name="plato"),
    path('vinf',views.vinf,name="vinf"),
    path('vsup',views.vsup,name="vsup"),
    path('biela',views.biela,name="biela"),
    path('pedal',views.pedal,name="pedal"),
    path('telescopio',views.telescopio,name="telescopio"),

    path('ruedas',views.ruedas,name="ruedas"),
    path('rayos',views.rayos,name="rayos"),
    path('buje',views.buje,name="buje"),
    path('llanta',views.llanta,name="llanta"),
    path('cubierta',views.cubierta,name="cubierta"),
    path('valvula',views.valvula,name="valvula"),
    path('piñones',views.piñones,name="piñones"),

    
    path('asiento',views.asiento,name="asiento"),
    path('sillin',views.sillin,name="sillin"),
    path('tija',views.tija,name="tija"),

    path('frenos',views.frenos,name="frenos"),
    path('fdel',views.fdel,name="fdel"),
    path('ftrac',views.ftrac,name="ftrac"),

    path('cambios',views.cambios,name="cambios"),
    path('cplato',views.cplato,name="cplato"),
    path('cpiñon',views.cpiñon,name="cpiñon"),

    path('accesorios',views.accesorios,name="accesorios"),
    path('cadena',views.cadena,name="cadena"),

    path('mas',views.mas,name="mas"),
]