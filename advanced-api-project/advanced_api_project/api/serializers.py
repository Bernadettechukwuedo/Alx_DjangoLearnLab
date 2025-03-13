from rest_framework import serializers
from .models import Book, Author
from datetime import datetime


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    # This validation ensures that the publication year is not in the future.
    def validate(self, data):
        if data["publication_year"] > datetime.now().year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return data


# This serializer includes the nested AuthorSerializer to display the author's name.
class AuthorSerializer(serializers.ModelSerializer):
    name = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["title", "publication_year", "author", "name"]
