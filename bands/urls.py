from django.urls import path
from . import views

urlpatterns = [
    path("musician/<int:musician_id>", views.musician, name= "musician"),
    path("musicians/", views.musicians, name="musicians"),
]
