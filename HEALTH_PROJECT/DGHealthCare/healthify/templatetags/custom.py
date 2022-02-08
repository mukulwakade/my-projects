from django import template

register = template.Library()

@register.filter(name='rupeesymbol')
def rupeesymbol(number):
    return "₹"+str(number)