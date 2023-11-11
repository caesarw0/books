from django.contrib import admin
from django.urls import path
# from book_api.views import book_list, book_create, book
from book_api.views import BookList, BookCreate, BookDetail

urlpatterns = [
    path('', BookCreate.as_view()),
    path('list/', BookList.as_view()), # list all books
    path('<int:pk>', BookDetail.as_view()) # getting a single book by it's pk
]