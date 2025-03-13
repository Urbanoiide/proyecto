from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length= 50)
    def __str__(self) -> str:
        return self.name
    
class Task(models.Model):
    titulo = models.CharField(max_length= 50)
    descripcion = models.TextField()
    project = models.ForeignKey(Project,  on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.titulo + ' - ' + self.project.name
    
class alumno(models.Model):
    nombre = models.CharField(max_length= 50)
    apellido = models.CharField(max_length= 50)
    def __str__(self) -> str:
        return self.nombre
    
class calificacion(models.Model):
    examen = models.IntegerField
    titulo = models.CharField(max_length= 50)
    descripcion = models.TextField()
    alumno = models.ForeignKey(alumno,  on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.titulo + ' - ' + self.alumno.nombre