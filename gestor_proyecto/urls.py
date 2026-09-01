from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("proyecto/", views.mostrar_proyectos, name="proyecto"),
    path('acercade/', views.acercade, name="acercade"),
    path("proyecto2/", views.mostrar_proyecto2, name="proyecto2"),
    path("nuevo-registro/", views.nuevo_registro, name="nuevo-registro"),
    path("cursos/", views.cursos, name="cursos"),
    path("proyectos/<int:id>/", views.ver_productos, name="ver-proyecto"),
    path("nuevo/nuevo/", views.nuevo_proyecto, name="nuevo-proyecto"),
    path('proyecto/<int:id>/eliminar/', views.eliminar_proyecto, name='eliminar_proyecto'),
    path('proyectos/<int:id>/editar', views.editar_proyecto, name='editar_proyecto'),
    path('proyectos/<int:proyecto_id>/tareas/nuevas/', views.crear_tarea, name='crear_tarea'),
    path('tareas/<int:id>/avanzar/', views.avanzar_estado_tarea, name='avanzar_estado_tarea'),
    path("proyectos/<int:id>/completar/",views.completar_proyecto,name="completar_proyecto"),
    path('tarea/<int:id>/eliminar/', views.eliminar_tarea, name='eliminar_tarea'),
    path("proyecto/", views.mostrar_proyectos, name="proyecto"),
]