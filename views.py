from django.shortcuts import render, redirect
from .models import Alumno, Asistencia
from .forms import AlumnoForm
from datetime import date
from django.shortcuts import get_object_or_404

def eliminar_alumno(request, alumno_id):
    alumno = get_object_or_404(Alumno, id=alumno_id)
    alumno.delete()
    return redirect('inicio')


def inicio(request):
    alumnos = Alumno.objects.all().order_by('numero_lista')
    asistencias = Asistencia.objects.filter(fecha=date.today())
    asistencia_dict = {a.alumno.id: a.presente for a in asistencias}

    return render(request, 'apiAsistencia/inicio.html', {
        'alumnos': alumnos,
        'asistencia': asistencia_dict
    })


def agregar_alumno(request):
    form = AlumnoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inicio')
    return render(request, 'apiAsistencia/agregar_alumno.html', {'form': form})


def pasar_lista(request):
    alumnos = Alumno.objects.all()

    if request.method == 'POST':
        Asistencia.objects.filter(fecha=date.today()).delete()

        for alumno in alumnos:
            presente = request.POST.get(str(alumno.id)) == 'on'
            Asistencia.objects.create(
                alumno=alumno,
                presente=presente
            )
        return redirect('inicio')

    return render(request, 'apiAsistencia/asistencia.html', {'alumnos': alumnos})
