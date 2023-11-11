from rest_framework import serializers
from book_api.models import Book
from django.forms import ValidationError

class BookSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = "__all__"

    def validate_title(self, value):
        if value == "Coke": # a dummy invalid book title
            raise ValidationError("No 'Coke' as a book title")
        return value
    
    def validate(self, data):
        if data["number_of_pages"] <= 0 or data["quantity"] <= 0:
            raise ValidationError("Invalid integer for `number_of_pages` or `quantity`, it must be > 0")
        return data
    
    def get_description(self, data):
        return "This book is called " + data.title + ", it's " + str(data.number_of_pages) + " pages long."