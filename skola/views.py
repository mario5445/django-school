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

def trieda(request, trieda):
    trieda_obj = Trieda.objects.get(nazov=trieda)
    studenti = Student.objects.filter(trieda_id=trieda_obj.pk).order_by("priezvisko")
    studenti_list = []
    for student in studenti:
        studenti_list.append(f'{student.meno} {student.priezvisko}')
    ucitel = Ucitel.objects.get(trieda_id=trieda_obj.pk)
    ucitel = f"{ucitel.titul} {ucitel.meno} {ucitel.priezvisko}"
    return render(request, "skola/trieda_list.html", {"trieda" : trieda, "ucitel" : ucitel, "studenti" : studenti_list})

def ucitel_detail(request, pk):
    ucitel = Ucitel.objects.get(pk=pk)
    return render(request, "skola/detail.html", {
        "ucitel" : ucitel,
    })

def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    triedny = Ucitel.objects.get(trieda_id=student.trieda_id)
    return render(request, "skola/detail.html", {
        "student" : student,
        "triedny" : triedny
    })