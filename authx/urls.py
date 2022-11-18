from rest_framework.routers import DefaultRouter
from django.urls.conf import include, path

from django.urls import re_path
from .viewsets import UserViewSet, LoginView

router = DefaultRouter()

router.register(
    r"users",
    UserViewSet,
    basename="users",
)

urlpatterns = [
    re_path(r"", include(router.urls)),
    path("login", LoginView.as_view(), name="login"),
]
