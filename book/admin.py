from django.contrib import admin
from .models import Book, BookComment, BookUser
# Register your models here.
admin.site.register(Book)
admin.site.register(BookComment)
admin.site.register(BookUser)
