from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import (
    filters as drf_filters,
)  # <-- this is for SearchFilter & OrderingFilter
from django_filters import rest_framework as django_filters


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [
        django_filters.DjangoFilterBackend,  # filtering by fields
        drf_filters.SearchFilter,  # search functionality
        drf_filters.OrderingFilter,  # ordering
    ]

    filterset_fields = ["title", "author", "publication_year"]
    search_fields = ["title", "author__name"]
    ordering_fields = ["title", "publication_year"]
    ordering = ["title"]


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
