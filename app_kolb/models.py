from django.db import models
class Pregunta(models.Model):
    DIMENSIONES = [
        ('EC', 'Experiencia Concreta'),
        ('OR', 'Observación Reflexiva'),
        ('CA', 'Conceptualización Abstracta'),
        ('EA', 'Experimentación Activa'),
    ]
    
    texto = models.TextField()
    dimension = models.CharField(max_length=2, choices=DIMENSIONES)
    orden = models.PositiveIntegerField(unique=True)  # Para controlar el orden de las preguntas

    def __str__(self):
        return f"Pregunta {self.orden} - {self.dimension}"

class Respuesta(models.Model):
    respuestas = models.JSONField(default=dict)  # Para almacenar las respuestas
    estilo_predominante = models.CharField(max_length=20, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def calcular_estilo(self):
        # Inicializamos los puntajes para cada dimensión
        puntajes = {
            'EC': 0,
            'OR': 0,
            'CA': 0,
            'EA': 0
        }
        # Calculamos los puntajes sumando las respuestas de cada dimensión
        for dimension in puntajes.keys():
            for pregunta, respuesta in self.respuestas.items():
                if Pregunta.objects.get(id=pregunta).dimension == dimension:
                    puntajes[dimension] += respuesta

        # Ordenamos las dimensiones por puntaje descendente
        dimensiones_ordenadas = sorted(puntajes.items(), key=lambda x: x[1], reverse=True)
        top1, top2 = dimensiones_ordenadas[0], dimensiones_ordenadas[1]

        # Determinamos el estilo según las combinaciones
        if (top1[0], top2[0]) in [('EC', 'EA'), ('EA', 'EC')]:
            estilo = "Acomodador"
        elif (top1[0], top2[0]) in [('CA', 'EA'), ('EA', 'CA')]:
            estilo = "Convergente"
        elif (top1[0], top2[0]) in [('EC', 'OR'), ('OR', 'EC')]:
            estilo = "Divergente"
        elif (top1[0], top2[0]) in [('CA', 'OR'), ('OR', 'CA')]:
            estilo = "Asimilador"
        else:
            estilo = "Híbrido"

        # Guardamos solo el estilo, no los puntajes
        self.estilo_predominante = estilo
        self.save()

        # Devolvemos el estilo y los puntajes para mostrarlos en el HTML
        return estilo, puntajes
