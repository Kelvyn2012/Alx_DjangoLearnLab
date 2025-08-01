from .views import BookViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r"books-all", BookViewSet, basename="book-all")


urlpatterns = [
    path("", include(router.urls)),
    path("token/", obtain_auth_token)
,
]
