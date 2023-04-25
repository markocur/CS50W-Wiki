from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("error", views.error, name="error"),
    path("wiki/<str:title>", views.entry, name="title"),
    path("new", views.new, name="new")
]
