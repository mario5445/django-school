from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.display_categories, name='display_categories'),
    path('posts/', views.display_posts, name='display_posts'),
    path('authors/', views.display_authors, name='display_authors'),
]
