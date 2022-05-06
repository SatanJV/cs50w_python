from Django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index")
]