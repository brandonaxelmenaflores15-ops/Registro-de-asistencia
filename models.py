from django.db import models

class Alumno(models.Model):
    numero_lista = models.IntegerField()
    nombre = models.CharField(max_length=100)
    grupo = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.numero_lista} - {self.nombre}"


class Asistencia(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    presente = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.alumno} - {self.fecha}"
