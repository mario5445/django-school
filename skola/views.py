from django.shortcuts import render, HttpResponse
from . models import Student

# Create your views here.
def vypis_student(request):
    studenti = list(Student.objects.all())
    return HttpResponse(studenti)