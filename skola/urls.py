from django.urls import path

from . import views

urlpatterns = [
    path("", views.vypis_student, name="vypis_student"),
]