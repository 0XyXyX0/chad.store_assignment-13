from rest_framework import serializers
from products.models import Product, Review, Cart, ProductTag, FavoriteProduct


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ["created_at", "updated_at"]


class ReviewModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class ProductTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTag
        fields = '__all__'


class FavoriteProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteProduct
        fields = '__all__'