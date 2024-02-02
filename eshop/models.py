from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.name}"

class Customer(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    premium = models.BooleanField(default=False)
    registered_at = models.DateTimeField(default=timezone.now)
    telephone = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.email} {self.username}"

# class Order_detail(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     total = models.DecimalField(max_digits=5, decimal_places=2)
#     created_at = models.DateTimeField(default=timezone.now)
    
#     def __str__(self) -> str:
#         return f"{self.customer} {self.total}"
    

# class Order_product(models.Model):
#     order = models.ForeignKey(Order_detail, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     created_at = models.DateTimeField(default=timezone.now)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.customer} {self.product}"