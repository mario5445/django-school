from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index_eshop"),
    path('products/', views.vypis_products, name="products"),
    path('categories/', views.vypis_categories, name="categories"),
    path('customers/', views.vypis_customers, name="customers"),
    path('categories/<category>/', views.category, name="category"),
    path('products/<product>', views.product, name="product")
]
