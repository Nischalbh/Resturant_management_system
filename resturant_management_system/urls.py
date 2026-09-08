from django.urls import path
from .views import category, Table, categorydetail

urlpatterns = [
    path("category/", category),
    path("category/<int:pk>/", categorydetail),
    path("table/", Table),
]
