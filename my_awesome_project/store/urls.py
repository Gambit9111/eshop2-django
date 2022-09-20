from django.urls import path
from .views import all_categories, products_by_category, product_detail, cart_view, checkout, payment

app_name = "store"
urlpatterns = [
    path("", all_categories, name="all_categories"),
    path("cart/", cart_view, name="cart_view"),
    path('checkout/', checkout, name="checkout"),
    path('payment/', payment, name="payment"),
    path('<slug:slug_cat>/', products_by_category, name="products_by_category"),
    path('<slug:slug_cat>/<slug:slug_prod>/', product_detail, name="product_detail"),
]