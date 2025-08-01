from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
