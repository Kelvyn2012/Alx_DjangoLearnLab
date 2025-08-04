from .views import BookViewSet, BookList
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r"books-all", BookViewSet, basename="book-all")


urlpatterns = [
    path("", include(router.urls)),
    path("books/", BookList.as_view(), name="book-list"),
    path("token/", obtain_auth_token),
]
