from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.auth.decorators import login_required



def order_create(request):
    """Выводит созданный заказ и очищает корзину"""
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         owner=request.user,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'orders/order/created_order.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create_order.html',
                  {'cart': cart, 'form': form})

@login_required
def orders(request):
    """Выводит страницу со всеми заказами пользователя"""
    orders_user = OrderItem.objects.filter(owner=request.user).all()
    context = {'orders': orders_user}
    return render(request, 'orders/order/orders.html', context)
