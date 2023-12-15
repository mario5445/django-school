from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('products/', views.vypis_products, name="products"),
    path('categories/', views.vypis_categories, name="categories"),
    path('customers/', views.vypis_customers, name="customers"),
]
