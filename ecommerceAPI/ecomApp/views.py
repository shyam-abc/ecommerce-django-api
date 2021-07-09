from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ecomApp.models import Category, Book, Product
from ecomApp.serializers import CategorySerializer, BookSerializer, ProductSerializer
# Create your views here.


class ListCategory(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DetailCategory(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListBook(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class DetailBook(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ListProduct(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DetailProduct(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
