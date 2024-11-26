from rest_framework import serializers

from .models import User, Book

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'personal_number', 'birth_date', 'full_name']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'genre', 'publication_date', 'stock_quantity']
