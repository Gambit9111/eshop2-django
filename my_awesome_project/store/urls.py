from django.urls import path
from .views import all_categories, products_by_category, product_detail, checkout, payment, order_item_endpoint, order_item_delete_endpoint
from django.views.generic import TemplateView

app_name = "store"
urlpatterns = [
    path("", all_categories, name="all_categories"),
    path("cart/", TemplateView.as_view(template_name="store/cart.html"), name="cart_view"),
    path('checkout/', checkout, name="checkout"),
    path('payment/', payment, name="payment"),

    path('<slug:slug_cat>/', products_by_category, name="products_by_category"),
    path('<slug:slug_cat>/<slug:slug_prod>/', product_detail, name="product_detail"),

    path('item/<slug:slug_cat>/<slug:slug_prod>/', order_item_endpoint, name="order_item_endpoint"),
    path('delete/<slug:slug_cat>/<slug:slug_prod>/<str:str>', order_item_delete_endpoint, name="order_item_delete_endpoint"),
]