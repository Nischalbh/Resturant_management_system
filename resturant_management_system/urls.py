from django.urls import path
from .views import category, Table, categorydetail, Table_detail

urlpatterns = [
    path("category/", category),
    path("category/<int:pk>/", categorydetail),
    path("table/", Table),
    path("table/<int:pk>", Table_detail),
]
