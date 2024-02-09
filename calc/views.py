from django.shortcuts import render, HttpResponse
from . models import *

# Create your views here.
def calc(request):
    if request.method == "GET":
        return render(request, "calc/index.html")
    if request.method == "POST":
        print(request.POST)
        try:
            a = float(request.POST['a'])
            b = float(request.POST['b'])
        except Exception:
            return render(request, "calc/index.html", { "error_message" : "Invalid input"})

        operator = request.POST['operator']
        if a == '' or b == '':
            return render(request, "calc/index.html", { "error_message" : "Vyplň všetky polia"})

        if operator == "+":
            vysledok = a + b
        elif operator == "-":
            vysledok = a - b
        elif operator == "*":
            vysledok = a * b
        elif operator == "/" and b != 0:
            vysledok = a / b
        else:
            return render(request, "calc/index.html", { "error_message" : "Nulou sa deliť nedá"})
        try:
            check = Priklad().objects.get(a=a, b=b, operator=operator)
        except:
            priklad = Priklad(a = a, b = b, operator = operator, vysledok = vysledok)
            priklad.save()
        return render(request, "calc/index.html", {"vysledok" : vysledok, "a":a, "b":b, "operator":operator})
    