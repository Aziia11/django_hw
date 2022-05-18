from django.urls import path
from . import views

urlpatterns =[
    path('books/', views.all_books),
    path('books/<int:id>/', views.get_book_detail),
]