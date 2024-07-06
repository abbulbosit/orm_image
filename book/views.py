from django.shortcuts import render
from .models import Book, Author, Comment


def home(request):
    return render(request, 'home.html')


def books(request):
    if request.method == 'POST':
        search = request.POST['search']
        book = Book.objects.filter(title__icontains=search) | Book.objects.filter(author__first_name__icontains=search)
        return render(request, 'book.html', {'books': book, "value": search})

    book = Book.objects.all()
    return render(request, 'book.html', {'books': book})


def authors(request):
    authors = Author.objects.all()
    return render(request, 'author.html', {'authors': authors})


def comments(request):
    comments = Comment.objects.all()
    return render(request, 'comments.html', {'comments': comments})

