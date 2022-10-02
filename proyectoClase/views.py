from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template, loader
import random

from home.models import Familia


def hola(request):
    return HttpResponse('Buena clase')


def fecha(request):
    fecha_y_hora = datetime.now()
    return HttpResponse(f'La fecha y hora actual es {fecha_y_hora}')


def calcular_fecha_nacimiento(request, edad):
    fecha = datetime.now().year - edad
    return HttpResponse(f'Tu fecha de nacimiento aproximada para tus {edad} años sería: {fecha}')


def mi_template(request):
    cargar_archivo = open(
        r'C:\Users\Juan Carlos Diaz\Desktop\MVTmiprimerproyecto\proyecto\template\template.html', 'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    contexto = Context()
    template_renderizado = template.render(contexto)
    return HttpResponse(template_renderizado)


def tu_template(request, nombre):
    # cargar_archivo = open(
    # r'C:\Users\Juan Carlos Diaz\Desktop\MVTmiprimerproyecto\proyecto\template\template.html', 'r')
    # template = Template(cargar_archivo.read())
    # cargar_archivo.close()
    # contexto = Context({'persona': nombre})
    # template_renderizado = template.render(contexto)

    template = loader.get_template("tu_template.html")
    template_renderizado = template.render({'persona': nombre})
    return HttpResponse(template_renderizado)


def prueba_template(request):

    mi_contexto = {'rango': list(range(1, 11)),
                   'valor_aleatorio': random.randrange(1, 11)

                   }
    template = loader.get_template('prueba_template.html')
    template_renderizado = template.render(mi_contexto)

    return HttpResponse(template_renderizado)


def crear_persona_template(request, nombre, apellido):

    familia = Familia(nombre=nombre, apellido=apellido,
                      edad=random.randrange(1, 99), fecha=datetime.now())
    familia.save()

    template = loader.get_template('crear_persona_template.html')
    template_renderizado = template.render({'familia': familia})

    return HttpResponse(template_renderizado)


def ver_personas_template(request):

    familias = Familia.objects.all()

    template = loader.get_template('ver_personas_template.html')
    template_renderizado = template.render({'familia': familias})

    return HttpResponse(template_renderizado)
