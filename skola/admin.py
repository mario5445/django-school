from django.contrib import admin
from . models import Student, Ucitel, Trieda

# Register your models here.
admin.site.register(Student)
admin.site.register(Ucitel)
admin.site.register(Trieda)