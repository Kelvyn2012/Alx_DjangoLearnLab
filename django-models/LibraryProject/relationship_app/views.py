from .models import Book, Library
from django.shortcuts import render
from django.views.generic.detail import DetailView


def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_details.html"
    context_object_name = "library"
