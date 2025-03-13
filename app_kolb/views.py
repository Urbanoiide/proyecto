from django.shortcuts import render, redirect
from .models import Respuesta,Pregunta
from django.contrib.auth.decorators import login_required

@login_required
def cuestionario(request):
    if request.method == 'POST':
        respuestas = {}
        for pregunta in Pregunta.objects.all():
            respuesta = request.POST.get(str(pregunta.id))
            if respuesta:  # Si la respuesta está presente
                respuestas[pregunta.id] = int(respuesta)
            else:
                respuestas[pregunta.id] = 0  # Si no se respondió, asignar 0 o algún valor por defecto

        # Guardar las respuestas
        respuesta = Respuesta.objects.create(respuestas=respuestas)

        # Calcular el estilo después de guardar
        estilo = respuesta.calcular_estilo()
        respuesta.estilo_predominante = estilo
        respuesta.save()

        # Redirigir a la página de resultados con el id de la respuesta
        return redirect('resultados', id=respuesta.id)

    preguntas = Pregunta.objects.all().order_by('orden')
    opciones = [
        (1, '1 - Totalmente en desacuerdo'),
        (2, '2 - En desacuerdo'),
        (3, '3 - Neutral'),
        (4, '4 - De acuerdo'),
        (5, '5 - Totalmente de acuerdo'),
    ]
    
    return render(request, 'cuestionario.html', {
        'preguntas': preguntas,
        'opciones': opciones,
    })
def resultados(request, id):
    respuesta = Respuesta.objects.get(id=id)
    
    # Calcular estilo y puntajes
    estilo, puntajes = respuesta.calcular_estilo()

    # Pasar tanto el estilo como los puntajes al template
    context = {
        'resultado': respuesta,
        'puntajes': puntajes,
    }
    return render(request, 'resultados.html', context)

    