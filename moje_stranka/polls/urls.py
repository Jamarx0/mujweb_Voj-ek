from django.urls import path

from . import views

urlpatterns = [
    path("as", views.index, name="index"),
]
