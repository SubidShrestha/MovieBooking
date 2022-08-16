from django.urls import path
from . import views

urlpatterns = [
    path('', views.getMovies),
    path("details/<int:id>", views.getMoviesDetails),
    path('add/', views.addMovies),
    path("update/<int:id>", views.updateMovies),
    path("delete/<int:id>", views.deleteMovies),
]
