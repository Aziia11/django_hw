from django.urls import path
from . import views

app_name = "books_url"
urlpatterns =[
    path('books/', views.all_books, name="books_all_url"),
    path('books/<int:id>/', views.get_book_detail, name="book"),
    path('add-book/', views.add_book, name="add_book"),
]
