from django.urls import path
from book_api.views import BookList, BookCreate, BookDetail

urlpatterns = [
    path('', BookCreate.as_view()), # endpoint: POST books/ to create a new book
    path('list/', BookList.as_view()), # endpoint: GET books/list/ to list all books
    path('<int:pk>', BookDetail.as_view()) # endpoint: GET books/1 to getting a single book by it's pk
]
