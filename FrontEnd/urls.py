from django.urls import include, path

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dia_1", views.dia_1, name="dia_1"),
    path("dia_5", views.dia_5, name="dia_5"),
]
