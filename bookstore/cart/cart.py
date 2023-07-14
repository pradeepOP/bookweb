from core.models import Book
from django.conf import settings


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]["book"] = Book.objects.get(pk=p)

        for item in self.cart.values():
            item["total_price"] = item["book"].price * item["quantity"]

            yield item

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def add(self, book_id, quantity=1, update_quantity=False):
        book_id = str(book_id)

        if book_id not in self.cart:
            self.cart[book_id] = {"quantity": 1, "id": book_id}

        if update_quantity:
            self.cart[book_id]["quantity"] += int(quantity)

            if self.cart[book_id]["quantity"] == 0:
                self.remove(book_id)

        self.save()

    def remove(self, book_id):
        if book_id in self.cart:
            del self.cart[book_id]
            self.save()

    def get_total_cost(self):
        for p in self.cart.keys():
            self.cart[str(p)]["book"] = Book.objects.get(pk=p)

        return sum(item["book"].price * item["quantity"] for item in self.cart.values())

    def get_item(self, book_id):
        if str(book_id) in self.cart:
            return self.cart[str(book_id)]
        else:
            return None
