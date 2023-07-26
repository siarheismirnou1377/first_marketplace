from .cart import Cart

def cart(request):
    """Котнтекстный процессор наличия товаров в корзине"""
    return {'cart': Cart(request)}