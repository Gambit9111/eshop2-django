from .models import Order

def get_order(request):
    try:
        device = request.COOKIES['device']
        order = Order.objects.get(device=device, completed=False)
    except:
        order = None
    return {"nav_order": order}