from .views import BookViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"books-all", BookViewSet, basename="book-all")


urlpatterns = [path("", include(router.urls))]
