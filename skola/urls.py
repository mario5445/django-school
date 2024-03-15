from django.urls import path

from . import views

urlpatterns = [
    path("", views.vypis_skola, name="vypis_skola"),
    path("studenti/", views.vypis_student, name="vypis_student"),
    path("ucitelia/", views.vypis_ucitel, name="vypis_ucitel"),
    path("triedy/", views.vypis_trieda, name="vypis_trieda"),
    path("triedy/<trieda>/", views.trieda, name="trieda"),
    path("ucitelia/<int:pk>/", views.ucitel_detail, name="ucitel_detail"),
    path("studenti/<int:pk>/", views.student_detail, name="student_detail"),
]