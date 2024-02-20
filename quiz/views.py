from django.shortcuts import render, HttpResponse
from calc.models import Priklad

# Create your views here.
def index(request):
    priklad = Priklad.objects.order_by('?').first()
    return render(request, "quiz/index.html", {
        "priklad" : priklad
    })