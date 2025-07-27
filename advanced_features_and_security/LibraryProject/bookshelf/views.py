# app/views.py
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from .models import Book
from .forms import BookForm, ExampleForm


@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = books.objects.all()
    return render(request, "book_list.html", {"books": books})


@permission_required("bookshelf.can_create", raise_exception=True)
@csrf_protect
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = request.user
            book.save()
            return redirect("article_list")
    else:
        form = BookForm()
    return render(request, "book_form.html", {"form": form})


@permission_required("bookshelf.can_edit", raise_exception=True)
@csrf_protect
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect("book_list")
    return render(request, "book_form.html", {"form": form})


@permission_required("bookshelf.can_delete", raise_exception=True)
@csrf_protect
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "confirm_delete.html", {"book": book})


@csrf_protect
def example_form_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # process form.cleaned_data
            return redirect("success_page")
    else:
        form = ExampleForm()
    return render(request, "form_example.html", {"form": form})
