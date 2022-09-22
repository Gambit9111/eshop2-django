from django.shortcuts import render, redirect
from .models import Category, Product, Order, OrderItem
from django.http import Http404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required


# categories view
def all_categories(request):
    # check if the url is valid
    try:
        categories = Category.get_all_categories()
    except:
        raise Http404("Kažkas negerai.. ")
    return render(request, "store/all_categories.html", {"categories": categories})


def products_by_category(request, slug_cat):
    try:
        products = Product.get_all_products_by_category_slug(slug_cat)
    except:
        raise Http404("Tokių grybų neradome.. ")
    return render(request, "store/products_by_category.html", {"products": products})


def product_detail(request, slug_cat, slug_prod):
    # check if the url is valid
    try:
        device = request.COOKIES['device']
        category = Category.objects.get(slug=slug_cat)
        product = Product.objects.get(slug=slug_prod)
        order, created = Order.objects.get_or_create(device=device, completed=False)
    except Product.DoesNotExist or Category.DoesNotExist:
        raise Http404("Tokių grybų neradome.. ")
    # get the device id
    # when user visits this page, check the database if there is NOT completed order with this device id
    # if there is NOT, create a new order with this device id
    # if there is, get that order

    # once we have order, lets check if there is order item with this product, if there is change the quantity and the price accordingly
    try:
        order_item = order.items.get(product=product)
    except OrderItem.DoesNotExist:
        order_item = None
    return render(request, "store/product_detail.html", {"product": product, "order_item": order_item})


# one endpoint managing order items
@require_http_methods(["POST"])
def order_item_endpoint(request, slug_cat, slug_prod):
    try:
    # get the device id and order and the product
        device = request.COOKIES['device']
        order = Order.objects.get(device=device, completed=False)
        product = Product.objects.get(slug=slug_prod)
    except:
        raise Http404("Kažkas negerai.. ")
    #if the order item exists, i change the quantity, otherwise i create a new order item
    try:
        order_item = order.items.get(product=product)
        order_item.quantity = request.POST['quantity']
        order_item.save()
    except OrderItem.DoesNotExist:
        OrderItem.objects.create(product=product, order=order, quantity=request.POST['quantity'])

    return redirect('store:product_detail', slug_cat=slug_cat, slug_prod=slug_prod)


def order_item_delete_endpoint(request, slug_cat, slug_prod, str):
    print(str)
    try:
        device = request.COOKIES['device']
        order = Order.objects.get(device=device, completed=False)
        product = Product.objects.get(slug=slug_prod)
    except:
        raise Http404("Kažkas negerai.. ")
    try:
        order_item = order.items.get(product=product)
        order_item.delete()
    except OrderItem.DoesNotExist:
        pass

    # ultra quick fix how to manage redirects after cart is empty. so now if i can add any string to the button and pass that to the url, i can make one
    # endpoint for all order management oh wait i cant because i can only send get requests
    if str == "cart":

        if order.items.first() == None:
            return redirect('store:all_categories')
        else:
            return redirect('store:cart_view')

    elif str == "product":
        return redirect('store:product_detail', slug_cat=slug_cat, slug_prod=slug_prod)
    
    # if the string is not cart or product something is fishy so just return to categories
    else:
        return redirect('store:all_categories')


def checkout(request, uuid):
    order = Order.objects.get(uuid=uuid)
    
    if request.method == "POST":
        data = request.POST
        print(data)

        order.name = (data['firstName'] + " " + data['lastName'])
        order.email = data['email']
        order.phone = data['phoneNumber']
        order.address = (data['address1'] + " " + data['address2'])
        order.city = data['city']
        order.completed = True

        order.save()

        return redirect('store:payment', uuid=uuid)

    return render(request, "store/checkout.html")

def payment(request, uuid):
    order = Order.objects.get(uuid=uuid)

    if request.method == "POST":
        order.paid = True
        order.save()
        return redirect('store:all_categories')

    return render(request, "store/payment.html", {"order": order})
