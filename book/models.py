from django.db import models
from django.contrib.auth.models import User
from .helpers import Change_name


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    image = models.ImageField(upload_to=Change_name.change)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    count = models.PositiveIntegerField(default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=Change_name.change)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    book = models.ManyToManyField(Book)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text}"



