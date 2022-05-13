from django.shortcuts import render
from django.http import  HttpResponse
from .models import Book
# Create your views here.
def book_world(request):
    return  HttpResponse("<h2>Book World<h2>")

def all_books(request):
    books = Book.objects.all()
    return render(request, "books.html", {"books": books})