from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from decimal import Decimal
from .models import Cart, CartItem
from products.models import Product


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart_detail")


@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)

    items = cart.items.all()

    subtotal = sum(item.total_price() for item in items)

    shipping = Decimal("0.00") if subtotal > Decimal("999.00") else Decimal("99.00")

    tax = subtotal * Decimal("0.05")

    total = subtotal + shipping + tax

    context = {
        "items": items,
        "subtotal": subtotal,
        "shipping": shipping,
        "tax": tax,
        "total": total,
    }

    return render(request, "cart/cart_detail.html", context)


@login_required
def increase_quantity(request, item_id):

    item = get_object_or_404(CartItem, id=item_id)

    item.quantity += 1
    item.save()

    return redirect("cart_detail")


@login_required
def decrease_quantity(request, item_id):

    item = get_object_or_404(CartItem, id=item_id)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect("cart_detail")


@login_required
def remove_item(request, item_id):

    item = get_object_or_404(CartItem, id=item_id)

    item.delete()

    return redirect("cart_detail")