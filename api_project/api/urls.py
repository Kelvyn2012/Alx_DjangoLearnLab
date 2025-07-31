from .views import BookListViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"books-all", BookListViewSet, basename="book-all")


urlpatterns = [path("", include(router.urls))]
