from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product, Review, Cart, FavoriteProduct, ProductTag
from rest_framework import status
from products.serializers import (
    ProductModelSerializer,
    ReviewModelSerializer,
    CartItemSerializer,
    ProductTagSerializer,
    FavoriteProductSerializer
    )


@api_view(['GET', 'POST'])
def products_view(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductModelSerializer(products, many=True)
        return Response(serializer.data)
    
    
    elif request.method == "POST":
        data = request.data
        serializer = ProductModelSerializer(data=request.data)

        if serializer.is_valid():
            product = serializer.save()
            return Response({"id": product.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



@api_view(["GET"])
def get_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductModelSerializer(product)
    return Response(serializer.data)




@api_view(['GET', 'POST'])
def cart_view(request):
    if request.method == 'GET':
        cart_items = Cart.objects.filter(user=request.user)
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'POST'])
def product_tag_view(request, product_id):
    if request.method == 'GET':
        tags = ProductTag.objects.filter(product_id=product_id)
        serializer = ProductTagSerializer(tags, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        request.data['product'] = product_id
        serializer = ProductTagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'POST'])
def favorite_product_view(request):
    if request.method == 'GET':
        favorites = FavoriteProduct.objects.filter(user=request.user)
        serializer = FavoriteProductSerializer(favorites, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = FavoriteProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
