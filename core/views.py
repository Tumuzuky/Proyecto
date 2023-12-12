from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def reporte_de_compras(request):
    return render(request, 'reportedecompras.html')

def reporte_de_ventas(request):
    return render(request, 'reportedeventas.html')

def agregar_proveedores(request):
    return render(request, 'agregarproveedores.html')

def agregar_producto(request):
    return render(request, 'agregarproducto.html')

def agregar_clientes(request):
    return render(request, 'agregarclientes.html')

# Create your views here.
