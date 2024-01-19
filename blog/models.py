from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    nazov = models.CharField(max_length=40)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return f"{self.nazov}"

class Author(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    registered_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.username}"

class Post(models.Model):
    nazov = models.CharField(max_length=60)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(default=timezone.now)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.nazov} {self.author}"
