from django.shortcuts import render, redirect,get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Proyecto, Curso,Tarea

@login_required
def home(request):
    return render(request, "home.html")


def acercade(requets):
    return render(requets,'acercade.html')
def mostrar_proyecto2(request):
    proyectos = Proyecto.objects.all()
    return render(request, "proyectos.html", {"proyectos": proyectos})

def mostrar_proyectos(request):
    proyectos = Proyecto.objects.all()
    nombres_proyectos = []
    for p in proyectos:
        nombres_proyectos.append(p.nombre)
    respuesta = "<br>".join(nombres_proyectos)
    return HttpResponse(respuesta)

def nuevo_registro(request):
    proyectos = [
        Proyecto(nombre="Sistema de Biblioteca", descripcion="Aplicación para administrar préstamos y devoluciones de libros.", duracion=120),
        Proyecto(nombre="Tienda Virtual", descripcion="Plataforma para la venta de productos en línea con carrito de compras.", duracion=180),
        Proyecto(nombre="Control de Inventario", descripcion="Sistema para registrar productos, entradas y salidas de un almacén.", duracion=90),
        Proyecto(nombre="Agenda Médica", descripcion="Aplicación para gestionar citas y pacientes en un consultorio.", duracion=150),
        Proyecto(nombre="Portal Académico", descripcion="Sistema para consultar notas, horarios y asignaturas.", duracion=200),
        Proyecto(nombre="Gestión de Empleados", descripcion="Aplicación para registrar empleados y controlar asistencia.", duracion=160),
        Proyecto(nombre="Restaurante Express", descripcion="Sistema para tomar pedidos y administrar el menú de un restaurante.", duracion=110),
        Proyecto(nombre="Reserva de Hoteles", descripcion="Plataforma para realizar reservas de habitaciones en línea.", duracion=210),
        Proyecto(nombre="Control de Vehículos", descripcion="Sistema para administrar vehículos, mantenimientos y conductores.", duracion=140),
        Proyecto(nombre="Gestión de Eventos", descripcion="Aplicación para organizar eventos, asistentes y cronogramas.", duracion=170)
    ]
    for p in proyectos:
        p.save()
    return HttpResponse("bien")

def ver_productos(request, id):
    proyecto = Proyecto.objects.get(id=id)
    return render(request, "detalle_proyecto.html", {"proyecto": proyecto})

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, "cursos.html", {"cursos": cursos})

def nuevo_proyecto(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        descripcion = request.POST["descripcion"]
        duracion = request.POST["duracion"]
        imagen = request.FILES.get('imagen')

        if nombre and descripcion and duracion and imagen:
            proyecto = Proyecto(
                nombre=nombre, 
                descripcion=descripcion, 
                duracion=duracion,
                imagen =imagen,
                )
            proyecto.save()
            

        return redirect("proyecto2")
    
    return render(request, "nuevo.html")
'''
def crear_proyecto(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        descripcion = request.POST["descripcion"]
        duracion = request.POST["duracion"]
        Proyecto.objects.create(nombre=nombre, descripcion=descripcion, duracion=duracion)
        return redirect("proyecto2")
    
    return render(request, "nuevo.html")
'''
def eliminar_proyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    proyecto.delete()
    return redirect('proyecto2')

def editar_proyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)

    if request.method == "POST":
        proyecto.nombre = request.POST.get("nombre")
        proyecto.descripcion = request.POST.get("descripcion")
        proyecto.duracion = request.POST.get("duracion")

        proyecto.save()

        return redirect("proyecto2")

    return render(
        request,
        "editar-proyecto.html",
        {"proyecto": proyecto}
    )

def crear_tarea(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)

    if request.method == "POST":
        titulo = request.POST.get("titulo", "").strip()
        prioridad = request.POST.get("prioridad")
        estado = request.POST.get("estado")

        if titulo:
            Tarea.objects.create(
                proyecto=proyecto,
                titulo=titulo,
                prioridad=prioridad,
                estado=estado
            )

            return redirect("/proyectos/" + str(proyecto.id) + "/")

    return render(request, "crear-tarea.html", {
        "proyecto": proyecto,
        "prioridad_choices": Tarea.PRIODIDAD_CHOICES,
        "estado_choices": Tarea.ESATADO_CHOICES
    })

@require_POST
def avanzar_estado_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)

    if tarea.estado == "PENDIENTE":
        tarea.estado = "PROCESO"

    elif tarea.estado == "PROCESO":
        tarea.estado = "COMPLETADO"

    tarea.save()

    return redirect("/proyectos/" + str(tarea.proyecto.id) + "/")

@require_POST
def completar_proyecto(request, id):

    proyecto = get_object_or_404(
        Proyecto,
        id=id
    )

    proyecto.estado = "COMPLETADO"
    proyecto.save()

    return redirect("proyecto2")


@require_POST
def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)

    id_proyecto = tarea.proyecto.id

    tarea.delete()

    return redirect("ver-proyecto", id=id_proyecto)