from django.urls import path
from .views import category, Table

urlpatterns = [path("category/", category), path("table/", Table)]
