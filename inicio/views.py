from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render  

def inicio(request):
    return HttpResponse("<h2> soy el inicio </h2>")

def vista_datos1(request, nombre):
    nombre_mayusucula= nombre.upper()
    return HttpResponse(f"holaa {nombre_mayusucula}!!")

def primer_template(request):
    fecha_actual=datetime.now()
    datos={ "fecha_actual":fecha_actual,
            "numeros":list(range (1, 11))}
    
    #v1
    #archivo_del_template= open(r"templates\primer_template.html")
    #template=Template(archivo_del_template.read())
    #archivo_del_template.close()
    #contexto=Context(datos)
    #render_template= template.render(contexto)
    
    #v2
    #template= loader.get_template("primer_template.html")
    #render_template=template.render(datos)
    #return HttpResponse(render_template)
    
    #v3
    return render(request,"primer_template.html", datos)