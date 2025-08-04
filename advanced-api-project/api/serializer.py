from .models import Author, Book
from rest_framework import serializers
import datetime


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def validate_publication_year(self, data):
        current_year = datetime.datetime.now().year
        if data > current_year:
            raise serializers.ValidationError(
                "ublication year cannot be in the future."
            )
        return data


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "books"]
