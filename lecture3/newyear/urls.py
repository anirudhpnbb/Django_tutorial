from django.urls import path
from . import views

# Write your urls here.


urlpatterns = [
    path("", views.index, name="index")
]