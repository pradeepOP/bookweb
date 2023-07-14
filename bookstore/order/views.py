from cart.cart import Cart
from django.shortcuts import redirect, render

from .models import Order, OrderItem


# Create your views here.
def start_order(request):
    cart = Cart(request)

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        zipcode = request.POST.get("zipcode")
        city = request.POST.get("city")
        phone = request.POST.get("phone")

        order = Order.objects.create(
            user=request.user,
            first_name=first_name,
            last_name=last_name,
            email=email,
            address=address,
            zipcode=zipcode,
            city=city,
            phone=phone,
        )

        for item in cart:
            book = item["book"]
            quantity = int(item["quantity"])
            price = book.price * quantity
            item = OrderItem.objects.create(
                order=order, book=book, price=price, quantity=quantity
            )

        return redirect("myaccount")
    return redirect("cart")
