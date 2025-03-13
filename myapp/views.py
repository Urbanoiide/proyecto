
from django.http import HttpResponse, JsonResponse
from .models import Project
from .models import Task
from django.shortcuts import get_object_or_404, render
# Create your views here.
def index(request):
    tittle = "Bienvenido!!"
    return render(request, 'index.html', {
        'tittle' : tittle
    })

def prueba(request):
    return HttpResponse("<h1>hola</h1>")

def about(request):
    acerca = "VARIABLE ACERCA"
    return render(request, 'about.html', {
        'about' : acerca
    })

def projects(request):
   # projects = list(Project.objects.values())
   # return JsonResponse(projects, safe=False)
    projects = Project.objects.all
    return render(request, 'project.html', {
        'projects' : projects
    })

def tasks(request):
    #task = get_object_or_404(Task, titulo=titulo)
    #return HttpResponse('tasks: %s' % task.titulo)
    return render(request, 'task.html')
