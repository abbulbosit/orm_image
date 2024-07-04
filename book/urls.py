from django.urls import path
from .views import home, authors, books, comments

urlpatterns = [
    path('', home, name='home'),
    path('authors/', authors, name='authors'),
    path('books/', books, name='books'),
    path('comments/', comments, name='comments'),
]
