from django.shortcuts import render
from .models import Category, Product

# categories view
def all_categories(request):
    categories = Category.get_all_categories()
    return render(request, "store/all_categories.html", {"categories": categories})

def products_by_category(request, slug_cat):
    products = Product.get_all_products_by_category_slug(slug_cat)
    return render(request, "store/products_by_category.html", {"products": products})

def product_detail(request, slug_cat, slug_prod):
    product = Product.objects.get(slug=slug_prod)
    device = request.COOKIES['device']

    if request.method == 'POST':
        quantity = request.POST['quantity']
        print(quantity)
        print(device)
    return render(request, "store/product_detail.html", {"product": product})

def cart_view(request):
    return render(request, "store/cart.html")