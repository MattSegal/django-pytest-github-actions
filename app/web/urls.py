from django.urls import path
from . import views

urlpatterns = [
    path("good-bye/", views.goodbye_view, name="goodbye"),
    path("", views.hello_view, name="hello"),
]
