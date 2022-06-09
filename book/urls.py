from django.urls import path
from . import views, models
from datetime import datetime, timedelta

start_date = datetime.today() - timedelta(days=3)

app_name = "books_url"
urlpatterns =[
    path('books/', views.BookListView.as_view(),  name="books_all_url"),
    path('books/latest/', views.BookListView.as_view(
        queryset=models.Book.objects.filter(
            created_date__gt=start_date
        ).order_by("-id")
    ), name="Latest"),
    path('books/adventure/', views.BookListView.as_view(
        queryset=models.Book.objects.filter(genre="Adventure").order_by("-id"),
    ), name="Adventure"),
    path('books/literaryfiction/', views.BookListView.as_view(
        queryset=models.Book.objects.filter(genre="Literary Fiction").order_by("-id"),
    ), name="Literary Fiction"),
    path('books/mystery/', views.BookListView.as_view(
        queryset=models.Book.objects.filter(genre="Mystery").order_by("-id"),
    ), name="Mystery"),
    path('books/thriller/', views.BookListView.as_view(
        queryset=models.Book.objects.filter(genre="Thriller").order_by("-id"),
    ), name="Thriller"),
    path('books/historical/', views.BookListView.as_view(
        queryset=models.Book.objects.filter(genre="Historical").order_by("-id"),
    ), name="Historical"),
    path('books/romance/', views.BookListView.as_view(
        queryset=models.Book.objects.filter(genre="Romance").order_by("-id"),
    ), name="Romance"),
    path('books/sciencefiction/', views.BookListView.as_view(
        queryset=models.Book.objects.filter(genre="Science Fiction").order_by("-id"),
    ), name="Science Fiction"),
    path('books/drama/', views.BookListView.as_view(
        queryset=models.Book.objects.filter(genre="Drama").order_by("-id"),
    ), name="Drama"),
    path('books/comedy/', views.BookListView.as_view(
        queryset=models.Book.objests.filter(genre="Comedy").order_by("id"),
    ), name="Comedy"),
    path('books/<int:id>/', views.BookDetailView.as_view(), name="book"),
    path('books/<int:id>/update/', views.BookUpdateView.as_view(), name="book_update"),
    path('books/<int:id>/delete/', views.BookDeleteView.as_view(), name="book_delete"),
    path('add-book/', views.BookCreateView.as_view(), name="add_book"),
]
