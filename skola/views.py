from django.shortcuts import render, HttpResponse
from . models import Student, Ucitel, Trieda

# Create your views here.

def vypis_skola(request):
    studenti = Student.objects.all().order_by("priezvisko")
    ucitelia = Ucitel.objects.all().order_by("priezvisko")
    triedy = Trieda.objects.all().order_by("nazov")
    return render(request, "skola/index.html", {
        "studenti" : studenti,
        "ucitelia" : ucitelia,
        "triedy" : triedy
    })

def vypis_student(request):
    studenti = Student.objects.all().order_by("priezvisko")
    return render(request, "skola/index.html", {
        "studenti" : studenti
    })

def vypis_ucitel(request):
    ucitelia = Ucitel.objects.all().order_by("priezvisko")
    return render(request, "skola/index.html", {
        "ucitelia" : ucitelia
    })

def vypis_trieda(request):
    triedy = Trieda.objects.all().order_by("nazov")
    return render(request, "skola/index.html", {
        "triedy" : triedy
    })