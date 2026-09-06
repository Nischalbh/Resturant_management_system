from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category
from .serializers import categorySerializers


# Create your views here.
@api_view()
def category(request):
    category = Category.objects.all()
    serializer = categorySerializers(category, many=True)
    return Response(serializer.data)
