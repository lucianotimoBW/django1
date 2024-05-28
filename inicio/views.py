from re import template
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader


def inicio(request):
    return HttpResponse('Bienvenido a mi INICIO!!!')

def template1(request):
    fecha = datetime.now()
    return HttpResponse(f'<h1>Mi Template 1</h1> -- fecha: {fecha}')



def template4(request, nombre, apellido, edad):
    suma = 4 + edad
    fecha = datetime.now()
    
    datos = {
        'fecha': fecha,
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad
    }

    return render(request, 'template4.html', datos)

def probando(request):
    lista = list(range(500))
    
    numeros = random.choises(lista, k=50)
    
    return render(request, 'probando_if_for.html', {'numeros': numeros})