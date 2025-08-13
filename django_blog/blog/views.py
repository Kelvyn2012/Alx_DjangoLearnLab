from django.shortcuts import render, redirect
from .models import Post
from .forms import customUserCreationForm, ProfileUpdateForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    return render(request, "home.html")


def register_view(request):
    if request.method == "POST":
        form = customUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = customUserCreationForm()

    return render(request, "blog/register.html", {"form": form})


@login_required
def profile_view(request):
    return render(request, "blog/profile.html")


@login_required
def edit_profile_view(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileUpdateForm(
            instance=request.user
        )  # ✅ prefill with current user data

    return render(request, "blog/edit_profile.html", {"form": form})
