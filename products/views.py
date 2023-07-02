from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Product
# Create your views here.

@api_view(["POST"])
def getcategories(r):
    categories = Category.objects.all()


    return Response(categories.values())


@api_view(["POST"])
def getcategoryproduct(r):
    data = r.data
    categoryid= data["category"]
    category = Category.objects.get(pk=categoryid)
    products = Product.objects.filter(product_category=category)


    return Response(products.values())