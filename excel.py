import os
import django
import random
import datetime
import csv


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from skola.models import *


studenti = Student.objects.all()
ucitelia = Ucitel.objects.all()
min_ucitel = 25
max_ucitel = 65

with open('ULICE.csv', mode ='r') as file:    
    csvFile = list(csv.reader(file, delimiter=';'))
    random.shuffle(csvFile)
    for student in studenti:
        adresa = csvFile.pop()
        student.ulica = adresa[0] + ' ' + str(random.randint(0,10))
        student.psc = adresa[1]
        student.mesto = adresa[2]
        student.save(update_fields=["ulica", "psc", "mesto"])
    for ucitel in ucitelia:
        adresa = csvFile.pop()
        ucitel.ulica = adresa[0] + ' ' + str(random.randint(0,10))
        ucitel.psc = adresa[1]
        ucitel.mesto = adresa[2]
        ucitel.save(update_fields=["ulica", "psc", "mesto"])



dni_v_mesiaci = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
triedy_roky = {
    "1" : 15,
    "2" : 16,
    "3" : 17,
    "4" : 18
}

def vypocitaj_dni_v_mesiaci(mesiac):
    dni = dni_v_mesiaci[mesiac-1]
    print(dni)
    if mesiac != 2:
        return random.randint(1, dni)
    else:
        year = datetime.date.today().year
        if (year % 4 == 0):
            if (year % 100 != 0):
                return random.randint(1, dni)
            elif (year % 100 == 0 and year % 400 == 0):
                return random.randint(1, dni)
            elif (year % 100 == 0 and year % 400 != 0):
                return random.randint(1, dni - 1)
        else:
            return random.randint(1, dni - 1)

for student in studenti:
    try:
        trieda = student.trieda.nazov[0]
        cislo_triedy = int(trieda)
    except Exception:
        print("Error occured")
        exit(1)
    rok = datetime.date.today().year - triedy_roky[trieda]
    mesiac = random.randint(1, 12)
    den = vypocitaj_dni_v_mesiaci(mesiac)
    student.datum_narodenia = f"{den}.{mesiac}.{rok}"
    student.save(update_fields=["datum_narodenia"])
    
for ucitel in ucitelia:
    this_year = datetime.date.today().year
    rok = random.randint(this_year - max_ucitel, this_year - min_ucitel)
    mesiac = random.randint(1, 12)
    den = vypocitaj_dni_v_mesiaci(mesiac)
    ucitel.datum_narodenia = f"{den}.{mesiac}.{rok}"
    ucitel.save(update_fields=["datum_narodenia"])

