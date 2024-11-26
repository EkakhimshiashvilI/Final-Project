from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    personal_number = models.CharField(max_length=50, unique=True)
    birth_date = models.DateField()
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    publication_date = models.DateField()
    stock_quantity = models.IntegerField()

    def __str__(self):
        return self.title


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reserved_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Reserved")

    def cancel_reservation(self):
        self.status = "Canceled"
        self.save()
