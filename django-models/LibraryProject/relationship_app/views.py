from .models import Book
from .models import Library, UserProfile
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test, login_required


def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"


class CustomLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


def check_role(role):
    def inner(user):
        return (
            user.is_authenticated
            and hasattr(user, "userprofile")
            and user.userprofile.role == role
        )

    return inner


@user_passes_test(check_role("Admin"))
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


@user_passes_test(check_role("Librarian"))
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


@user_passes_test(check_role("Member"))
def member_view(request):
    return render(request, "relationship_app/member_view.html")
