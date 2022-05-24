from django.urls import path
from . import views

app_name = "books_url"
urlpatterns =[
    path('books/', views.all_books, name="books_all_url"),
    path('books/latest', views.book_latest, name="Latest"),
    path('books/adventure', views.book_adventure, name="Adventure"),
    path('books/literaryfiction', views.book_literaryfiction, name="Literary Fiction"),
    path('books/mystery', views.book_mystery, name="Mystery"),
    path('books/thriller', views.book_thriller, name="Thriller"),
    path('books/historical', views.book_historical, name="Historical"),
    path('books/romance', views.book_romance, name="Romance"),
    path('books/sciencefiction', views.book_sciencefiction, name="Science Fiction"),
    path('books/drama', views.book_drama, name="Drama"),
    path('books/comedy', views.book_comedy, name="Comedy"),
    path('books/<int:id>/', views.get_book_detail, name="book"),
    path('books/<int:id>/update/', views.book_update, name="book_update"),
    path('books/<int:id>/delete/', views.book_delete, name="book_delete"),
    path('add-book/', views.add_book, name="add_book"),
]
