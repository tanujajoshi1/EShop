from django import template

register= template.Library()
#register ia a decorator here
@register.filter(name='item_in_cart')
def item_in_cart(product, cart):
    keys=cart.keys()
    for id in keys:
        try:
            id = int(id)
        except ValueError:
            return False
        if id==product.id:
            return True       
        
        else:
            return False