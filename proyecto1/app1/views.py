from django.shortcuts import render, HttpResponse

# Create your views here.
def inicio(request):

    return render(request,"app1/inicio.html")

def piezas(request):
    
    return render(request,"app1/piezas.html")

def comentarios(request):
    
    return render(request,"app1/comentarios.html")

def estadisticas(request):
    
    return render(request,"app1/estadisticas.html")