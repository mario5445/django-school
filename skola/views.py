from django.shortcuts import render, HttpResponse
from . models import *
from dateutil import relativedelta
# from datetime import datetime as dt
import datetime
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
        studenti_list.append(student)
    ucitel = Ucitel.objects.get(trieda_id=trieda_obj.pk)
    return render(request, "skola/trieda_list.html", {"trieda" : trieda, "ucitel" : ucitel, "studenti" : studenti_list})

def ucitel_detail(request, pk):
    ucitel = Ucitel.objects.get(pk=pk)
    try:
        kruzok = Kruzok.objects.get(ucitel=ucitel.id)
    except Exception:
        kruzok = None
    start_date = datetime.date.today()
    end_date = datetime.datetime.strptime(ucitel.datum_narodenia, "%d.%m.%Y") 
    vek = abs(relativedelta.relativedelta(end_date, start_date).years)
    return render(request, "skola/detail.html", {
        "ucitel" : ucitel,
        "kruzky_ucitel" : kruzok,
        "vek" : vek
    })

def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    triedny = Ucitel.objects.get(trieda_id=student.trieda_id)
    kruzky = Kruzok.objects.all().filter(student=student.id)
    start_date = datetime.date.today()
    end_date = datetime.datetime.strptime(student.datum_narodenia, "%d.%m.%Y") 
    vek = abs(relativedelta.relativedelta(end_date, start_date).years)
    return render(request, "skola/detail.html", {
        "student" : student,
        "triedny" : triedny,
        "kruzky" : kruzky,
        "vek" : vek
    })

def vypis_kruzky(request):
    kruzky = Kruzok.objects.all().order_by("nazov")
    return render(request, "skola/index.html", {
        "kruzky" : kruzky
    })

def kruzok_detail(request, skr):
    kruzok = Kruzok.objects.get(skratka=skr)
    studenti = Student.objects.all().filter(kruzok=kruzok.pk)
    return render(request, "skola/detail.html", {
        "kruzok" : kruzok,
        "studenti" : studenti
    })