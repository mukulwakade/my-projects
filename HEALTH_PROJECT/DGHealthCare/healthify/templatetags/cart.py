from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False

@register.filter(name='cart_count')
def cart_count(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0


@register.filter(name="quantity")
def quantity(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0


@register.filter(name="total")
def total(product,cart):
    return product.price * quantity(product,cart)

@register.filter(name="grandtotal")
def grandtotal(cartproducts,cart):
    sum = 0
    for p in cartproducts:
        sum += total(p,cart)
    return sum