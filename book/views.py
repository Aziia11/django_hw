
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from . import models, forms
# Create your views here.
def book_world(request):
    return  HttpResponse("<h2>Book World<h2>")

def all_books(request):
    books = models.Book.objects.all()
    return render(request, "books.html", {"books": books})

def get_book_detail(request, id):
    object = get_object_or_404(models.Book, id=id)
    return render(request, "book_detail.html", {"book": object})

def add_book(request):
    method = request.method
    if method == "POST":
        form = forms.MasterpieceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Masterpiece Created successfully!")
            #return redirect(reverse("books_url:books_all_url"))
    else:
        form = forms.MasterpieceForm()
    return render(request, "add_books.html", {"form": form})