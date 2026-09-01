from django.db import models

class  Proyecto(models.Model):
    '''
    Modelo que representa un proyecto
    '''

    nombre = models.CharField(max_length=100) #campo de texto varchar
    descripcion = models.TextField() #campo de texto largo
    duracion = models.IntegerField() # campo entero
    imagen = models.ImageField(upload_to='img/', default='img/Logo.png')

from django.db import models

class Tarea(models.Model):
    '''
    Modelo que representa una tarea de un proyecto
    '''
    PRIODIDAD_CHOICES ={
        ('BAJA','Baja'),
        ('MEDIA','Media'),
        ('ALTA','Alta'),
    }

    ESATADO_CHOICES={
        ('PENDIENTE','Pendiente'),
        ('PROCESO','En progreso'),
        ('COMPLETADO','Completado'),
    }

    # uno a mucho
    proyecto=models.ForeignKey(
        Proyecto,
        on_delete=models.CASCADE,
        related_name='tareas'
    )

    titulo=models.CharField(max_length=50)
    prioridad=models.CharField(max_length=5, choices=PRIODIDAD_CHOICES, default='MEDIA')
    estado=models.CharField(max_length=15, choices=ESATADO_CHOICES, default='PROCESO')
class Curso(models.Model):
    '''
    Modelo que representa un curso
    '''

    Materia = models.CharField(max_length=100)   # campo de texto varchar
    instructor = models.CharField(max_length=50) # nombre del instructor
    cupos = models.IntegerField()               # cantidad de cupos disponibles
