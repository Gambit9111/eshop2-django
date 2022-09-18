from django.shortcuts import render
from .models import Category

# categories view
def all_categories(request):
    categories = Category.get_all_categories()
    return render(request, "store/all_categories.html", {"categories": categories})