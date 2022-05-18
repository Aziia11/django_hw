
from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponse
from .models import Book
# Create your views here.
def book_world(request):
    return  HttpResponse("<h2>Book World<h2>")

def all_books(request):
    books = Book.objects.all()
    return render(request, "books.html", {"books": books})

def get_book_detail(request, id):
    object = get_object_or_404(Book, id=id)
    return render(request, "book_detail.html", {"book": object})