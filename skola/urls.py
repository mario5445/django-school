from django.urls import path

from . import views

urlpatterns = [
    path("", views.vypis_skola, name="vypis_skola"),
    path("studenti/", views.vypis_student, name="vypis-student"),
    path("ucitelia/", views.vypis_ucitel, name="vypis-ucitel"),
    path("triedy/", views.vypis_trieda, name="vypis-trieda"),
]