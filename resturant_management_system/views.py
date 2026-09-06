from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category
from .serializers import categorySerializers, TableSerializers
from .models import Table as TableModel


# Create your views here.
@api_view()
def category(request):
    category = Category.objects.all()
    serializer = categorySerializers(category, many=True)
    return Response(serializer.data)


@api_view()
def Table(request):
    table = TableModel.objects.all()
    serializer = TableSerializers(table, many=True)
    return Response(serializer.data)
