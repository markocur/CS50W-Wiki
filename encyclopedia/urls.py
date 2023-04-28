from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("error", views.error, name="error"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("random", views.random, name="random"),
    path("new", views.new, name="new"),
    path("wiki/edit/<str:title>", views.edit, name="edit")
]
