from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')

def helado(request):
    return render(request, 'helado.html')

def galletas(request):
    return render(request, 'galletas.html')

def frutas(request):
    return render(request, 'frutas.html')

def ensaladas(request):
    return render(request, 'ensaladas.html')

def comidas(request):
    return render(request, 'comidas.html')

def burritos(request):
    return render(request, 'burritos.html')