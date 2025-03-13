from django.contrib import admin
from .models import Project, Task, alumno, calificacion
# Register your models here.
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(alumno)
admin.site.register(calificacion)