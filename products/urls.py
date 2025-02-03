from django.urls import path
from products.views import products_view, get_product, cart_view, product_tag_view, favorite_product_view


urlpatterns = [
    path("products/", products_view, name='products'),
    path("products/<int:pk>/", get_product, name="product"),
    path('cart/', cart_view, name='cart_view'),
    path('products/<int:product_id>/tags/', product_tag_view, name='product_tag_view'),
    path('favorites/', favorite_product_view, name='favorite_product_view'),
]