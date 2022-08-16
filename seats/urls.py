from django.urls import path

from .models import bookedseat
from . import views

urlpatterns = [
    path('', views.getSeats),
    path("details/<int:id>", views.getSeatsDetails),
    path('add/', views.addSeats),
    path("update/<int:id>", views.updateSeats),
    path("delete/<int:id>", views.deleteSeats),

    # bookedseats
    path('booked/', views.getBookedSeats),
    path("booked/details/<int:id>", views.getBookedSeatsDetails),
    path('booked/add/', views.addBookedSeats),
    path("booked/update/<int:id>", views.updateBookedSeats),
    path("booked/delete/<int:id>", views.deleteBookedSeats),
]
