from django.urls import path
from . import views

# Write your urls here.

app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add")
]