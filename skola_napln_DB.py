import os
import django
import random


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from skola.models import *

Trieda.objects.all().delete()
Ucitel.objects.all().delete()
Student.objects.all().delete()

triedy = []
for rocnik in range(1, 5):
    for trieda in ['A', 'B', 'C', 'D']:
        triedy.append(f'{rocnik}.{trieda}')
        Trieda.objects.create(nazov=f'{rocnik}.{trieda}')

print(triedy)

fmena = open('mena.txt', 'r', encoding='utf-8')
mena = fmena.read().splitlines()
fmena.close()
print(mena)

fpriezviska = open('priezviska.txt', 'r', encoding="utf-8")
priezviska = fpriezviska.read().splitlines()
fpriezviska.close()
print(priezviska)

for i in range(20):
    meno = random.choice(mena)
    priezvisko = random.choice(priezviska)
    titul = random.choice(["Mgr.", "PhDr.", "Ing.", "RNDr.", "PaeDr.", ""])
    
    if i < len(triedy):
        trieda = Trieda.objects.get(nazov=triedy[i])
        Ucitel.objects.create(meno=meno, priezvisko=priezvisko, titul=titul, trieda=trieda)
    else:
        Ucitel.objects.create(meno=meno, priezvisko=priezvisko, titul=titul)        
        
for i in range(100):
    meno = random.choice(mena)
    priezvisko = random.choice(priezviska)
    titul = random.choice(["Mgr.", "PhDr.", "Ing.", "RNDr.", "PaeDr.", ""])

    trieda = Trieda.objects.get(nazov=random.choice(triedy))
    Student.objects.create(meno=meno, priezvisko=priezvisko, trieda=trieda)
        
        
