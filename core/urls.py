from .views import get_page

from django.urls import path

urlpatterns = [
    path("", get_page, name="home"),
]
