from django.contrib import admin
from .models import Book, Author, Comment
#
# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(Comment)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'content')
    list_display_links = ('id', 'author')
    search_fields = ('content', "author")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", 'title', "author")
    list_display_links = ("id", 'title', "author")
    search_fields = ("id", "title", "description", "author")
    ordering = ("id",)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name"]
    list_display_link = ["id", "first_name", "last_name"]
    search_fields = ("id", "first_name", "last_name")
    # group_by = ("id",)
