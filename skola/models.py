from django.db import models

# Create your models here.

class Trieda(models.Model):
    nazov = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Trieda"
        verbose_name_plural = "Triedy"
        ordering = ["nazov"]

    def __str__(self) -> str:
        return f"{self.nazov}"


class Ucitel(models.Model):
    titul = models.CharField(max_length=20)
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    trieda = models.ForeignKey(Trieda, on_delete=models.SET_NULL, null=True, blank=True)
    ulica = models.CharField(max_length=64, null=True, blank=True)
    psc = models.CharField(max_length=6, null=True, blank=True)
    mesto = models.CharField(max_length=32, null=True, blank=True)
    datum_narodenia = models.CharField(max_length=11, null=True, blank=True)

    class Meta:
        verbose_name = "Učiteľ"
        verbose_name_plural = "Učitelia"
        ordering = ["priezvisko"]

    def __str__(self):
        if self.trieda:
            return f"{self.titul} {self.meno} {self.priezvisko} {self.trieda}"
        else:
            return f"{self.titul} {self.meno} {self.priezvisko}"


class Kruzok(models.Model):
    nazov = models.CharField(max_length=100)
    skratka = models.CharField(max_length=3)
    ucitel = models.ForeignKey(Ucitel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Krúžok"
        verbose_name_plural = "Krúžky"
        ordering = ["nazov"]
  

    def __str__(self) -> str:
        return f"{self.nazov}"


class Student(models.Model):
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    trieda = models.ForeignKey(Trieda, on_delete=models.SET_NULL, null=True, blank=True)
    kruzok = models.ManyToManyField(Kruzok, null=True, blank=True)
    ulica = models.CharField(max_length=64, null=True, blank=True)
    psc = models.CharField(max_length=6, null=True, blank=True)
    mesto = models.CharField(max_length=32, null=True, blank=True)
    datum_narodenia = models.CharField(max_length=11, null=True, blank=True)
    
    class Meta:
        verbose_name = "Študent"
        verbose_name_plural = "Študenti"
        ordering = ["priezvisko"]

    def __str__(self):
        return f"{self.meno} {self.priezvisko} {self.trieda}"
    
class Uzivatel(models.Model):
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    email = models.EmailField()
    datum = models.DateField()

    def __str__(self) -> str:
        return f"{self.meno} {self.priezvisko}"
    
    class Meta:
        verbose_name = "Užívateľ"
        verbose_name_plural = "Užívatelia"
        ordering = ["priezvisko", "meno"]