from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Book, UserProfile


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]


class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )

    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')  # Don't include 'role'

    def save(self, commit=True):
        user = super().save(commit)
        role = self.cleaned_data['role']
        # Assign role to userprofile
        user_profile = user.userprofile
        user_profile.role = role
        user_profile.save()
        return user

