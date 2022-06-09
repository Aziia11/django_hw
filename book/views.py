
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from . import models, forms
from datetime import datetime, timedelta
from django.views import generic

start_date = datetime.today() - timedelta(days=3)
# Create your views here.

class BookListView(generic.ListView):
    template_name = "books.html"
    queryset = models.Book.objects.order_by("-id")

    def get_queryset(self):
        return self.queryset




# def book_world(request):
#     return  HttpResponse("<h2>Book World<h2>")
#
# def all_books(request):
#     books = models.Book.objects.order_by("-id")
#     return render(request, "books.html", {"books": books})
#
# def book_latest(request):
#     books = models.Book.objects.filter(created_date__gt=start_date).order_by("-id")
#     return render(request, "books.html", {"books": books})
#
# def book_adventure(request):
#     books = models.Book.objects.filter(genre="Adventure").order_by("-id")
#     return render(request, "books.html", {"books": books})
#
# def book_literaryfiction(request):
#     books = models.Book.objects.filter(genre="Literary Fiction").order_by("-id")
#     return render(request, "books.html", {"books": books})
#
# def book_mystery(request):
#     books = models.Book.objects.filter(genre="Mystery").order_by("-id")
#     return render(request, "books.html", {"books": books})
#
# def book_thriller(request):
#     books = models.Book.objects.filter(genre="Thriller").order_by("-id")
#     return render(request, "books.html", {"books": books})
#
# def book_historical(request):
#     books = models.Book.objects.filter(genre="Historical").order_by("-id")
#     return render(request, "books.html", {"books": books})
#
# def book_romance(request):
#     books = models.Book.objects.filter(genre="Romance").order_by("-id")
#     return render(request, "books.html", {"books": books})
#
# def book_sciencefiction(request):
#     books = models.Book.objects.filter(genre="Science Fiction").order_by("-id")
#     return render(request, "books.html", {"books": books})
#
# def book_drama(request):
#     books = models.Book.objects.filter(genre="Drama").order_by("-id")
#     return render(request, "books.html", {"books": books})
#
# def book_comedy(request):
#     books = models.Book.objects.filter(genre="Comedy").order_by("-id")
#     return render(request, "books.html", {"books": books})
class BookDetailView(generic.DetailView):
    template_name = "book_detail.html"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)
# def get_book_detail(request, id):
#     object = get_object_or_404(models.Book, id=id)
#     return render(request, "book_detail.html", {"book": object})

class BookCreateView(generic.CreateView):
    template_name = "add_books.html"
    form_class = forms.MasterpieceForm
    queryset = models.Book.objects.all()
    success_url = "/books/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super (BookCreateView, self).form_valid(form=form)
# def add_book(request):
#     method = request.method
#     if method == "POST":
#         form = forms.MasterpieceForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             #return HttpResponse("Masterpiece Created successfully!")
#             return redirect(reverse("books_url:books_all_url"))
#     else:
#         form = forms.MasterpieceForm()
#     return render(request, "add_books.html", {"form": form})

class BookUpdateView(generic.UpdateView):
    template_name = "book_update.html"
    form_class = forms.MasterpieceForm
    success_url = "/books/"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=book_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookUpdateView, self).form_valid(form=form)
# def book_update(request, id):
#     book_object = get_object_or_404(models.Book, id=id)
#     if request.method == "POST":
#         form = forms.MasterpieceForm(instance=book_object, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("books_url:books_all_url"))
#     else:
#         form = forms.MasterpieceForm(instance=book_object)
#     return render(request, "book_update.html", {"form": form,
#                                                 "object": book_object})
class BookDeleteView(generic.DeleteView):
    success_url = "/books/"
    template_name = "confirm_delete_html"

    def get_object(self, **kwargs):
        books_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=books_id)
# def book_delete(request, id):
#     book_object = get_object_or_404(models.Book, id=id)
#     book_object.delete()
#     return redirect(reverse("books_url:books_all_url"))



