from rest_framework.views import APIView
from book_api.models import Book
from book_api.serializer import BookSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class BookList(APIView): # inherit the APIView
    # GET method logic
    def get(self, request):
        books = Book.objects.all() # complex data
        serializer = BookSerializer(books, many=True) # return JSON
        return Response(serializer.data)
    
class BookCreate(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data) # from JSON to complex data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class BookDetail(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    def put(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        # setting restriction on removing the initial books
        if pk == 1 or pk == 2:
            return Response({'error': 'cannot remove the initial book with pk = 1 or pk = 2'}, 
                            status=status.HTTP_403_FORBIDDEN)
        else:
            book = get_object_or_404(Book, pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
