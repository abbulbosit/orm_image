from django.shortcuts import render
from .models import Book, Author, Comment


def home(request):
    return render(request, 'home.html')


def books(request):
    book = Book.objects.all()
    return render(request, 'book.html', {'books': book})


def authors(request):
    authors = Author.objects.all()
    return render(request, 'author.html', {'authors': authors})

def comments(request):
    comments = Comment.objects.all()
    return render(request, 'comments.html', {'comments': comments})
