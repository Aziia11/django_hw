from django.db import models

# Create your models here.
class Book(models.Model):
        GENRE_CHOICE = (
                ("Adventure", "Adventure"),
                ("Literary Fiction", "Literary Fiction"),
                ("Mystery", "Mystery"),
                ("Thriller", "Thriller"),
                ("Historical", "Historical"),
                ("Romance", "Romance"),
                ("Science Fiction", "Science Fiction"),
                ("Drama", "Drama"),
                ("Comedy", "Comedy")
        )
        title = models.CharField(max_length=100)
        description = models.TextField()
        image = models.ImageField(upload_to="media")
        genre = models.CharField(max_length=100, choices=GENRE_CHOICE)
        quantity_of_page = models.PositiveIntegerField()
        author = models.CharField(max_length=100)
        created_date = models.DateField(auto_now_add=True)
        updated_date = models.DateField(auto_now=True)

        def __str__(self):
                return self.title