from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("entry/<str:entry>", views.entry, name="entry"),
    path("query_results", views.query_results, name="query_results"),
    path("add_new", views.add_new, name="add_new"),
    path("entry/<str:entry>/edit", views.edit, name="edit"),
    path("random", views.random, name="random")
]
