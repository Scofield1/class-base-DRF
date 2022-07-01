from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from products.models import Product
from rest_framework import generics


class ProductDetailApiView(generics.RetrieveAPIView):
    qs = Product.objects.all()

