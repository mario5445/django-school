from django.db import models

# Create your models here.

class Trieda(models.Model):
    nazov = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Trieda"
        verbose_name_plural = "Triedy"

    def __str__(self) -> str:
        return f"{self.nazov}"


class Student(models.Model):
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    trieda = models.ForeignKey(Trieda, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        verbose_name = "Študent"
        verbose_name_plural = "Študenti"

    def __str__(self):
        return f"{self.meno} {self.priezvisko} {self.trieda}"

class Ucitel(models.Model):
    titul = models.CharField(max_length=20)
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    trieda = models.ForeignKey(Trieda, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Učiteľ"
        verbose_name_plural = "Učitelia"

    def __str__(self):
        if self.trieda:
            return f"{self.meno} {self.priezvisko} {self.trieda}"
        else:
            return f"{self.meno} {self.priezvisko}"

