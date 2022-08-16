from django.urls import path
from . import views

urlpatterns = [
    path('', views.getUsers),
    path("details/<int:id>", views.getUsersDetails),
    path('add/', views.addUsers),
    path("update/<int:id>", views.updateUsers),
    path("delete/<int:id>", views.deleteUsers),
]
