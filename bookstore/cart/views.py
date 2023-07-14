from core.models import Book
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .cart import Cart


def add_to_cart(request, book_id):
    cart = Cart(request)
    cart.add(book_id)
    return render(request, "cart/menu_cart.html")


def cart(request):
    return render(request, "cart/cart.html")


def update_cart(request, book_id, action):
    cart = Cart(request)

    if action == "increment":
        cart.add(book_id, 1, True)

    else:
        cart.add(book_id, -1, True)

    book = Book.objects.get(pk=book_id)
    quantity = cart.get_item(book_id)

    if quantity:
        quantity = quantity["quantity"]

        item = {
            "book": {
                "id": book.id,
                "title": book.title,
                "cover_image": book.cover_image,
                "price": book.price,
            },
            "total_price": (quantity * book.price),
            "quantity": quantity,
        }

    else:
        item = None

    response = render(request, "cart/partials/cart_item.html", {"item": item})
    response["HX-Trigger"] = "update-menu-cart"
    return response


@login_required(login_url="login")
def checkout(request):
    return render(request, "cart/checkout.html")


def hx_menu_cart(request):
    return render(request, "cart/menu_cart.html")


def hx_cart_total(request):
    return render(request, "cart/partials/cart_total.html")
