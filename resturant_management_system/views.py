from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category, OrderItem
from .serializers import categorySerializers, TableSerializers
from .models import Table as TableModel


# Create your views here.
@api_view(["GET", "POST"])
def category(request):
    if request.method == "GET":
        category = Category.objects.all()
        serializer = categorySerializers(category, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = categorySerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
def categorydetail(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == "GET":
        serializer = categorySerializers(category)
        return Response(serializer.data)
    elif request.method == "DELETE":
        item = OrderItem.objects.filter(food_category=category).count()
        if item > 0:
            return Response({"message": "can not be related to food in orderItem."})
        category.delete()
        return Response({"message": "Data deleted."})
    elif request.method == "PUT":
        serializer = categorySerializers(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view()
def Table(request):
    table = TableModel.objects.all()
    serializer = TableSerializers(table, many=True)
    return Response(serializer.data)
