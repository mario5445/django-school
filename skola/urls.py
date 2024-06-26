from django.urls import path

from . import views

urlpatterns = [
    path("", views.vypis_skola, name="vypis_skola"),
    path("studenti/", views.vypis_student, name="vypis_student"),
    path("ucitelia/", views.vypis_ucitel, name="vypis_ucitel"),
    path("triedy/", views.vypis_trieda, name="vypis_trieda"),
    path("kruzky/", views.vypis_kruzky, name="vypis_kruzok"),
    path("triedy/<trieda>/", views.trieda, name="trieda"),
    path("ucitelia/<int:pk>/", views.ucitel_detail, name="ucitel_detail"),
    path("studenti/<int:pk>/", views.student_detail, name="student_detail"),
    path("kruzky/<skr>/", views.kruzok_detail, name="kruzok_detail"),
    path("add_uzivatel/", views.pridaj_uzivatel, name="pridaj_uzivatel"),
    path("add_uzivatel/", views.pridaj_uzivatel2, name="pridaj_uzivatel2"),
]