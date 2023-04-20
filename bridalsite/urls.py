from django.urls import path

from . import views

urlpatterns = [
    path("", views.indexfeature, name = "index"),
    path("", views.indexlatest, name = "index")
]