from django.db import models

# Create your models here.
class Student(models.Model):
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    trieda = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.meno} {self.priezvisko} {self.trieda}"

class Ucitel(models.Model):
    titul = models.CharField(max_length=20)
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    trieda = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Učiteľ"
        verbose_name_plural = "Učitelia"

    def __str__(self):
        return f"{self.titul} {self.meno} {self.priezvisko} {self.trieda}"


