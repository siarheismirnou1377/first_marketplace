from django.shortcuts import get_object_or_404, render
from .models import Category, Product
from cart.forms import CartAddProductForm


def index(request):
    """Главная страница"""
    return render(request, 'marketplaces/index.html')

def categories(request):
    """Выводит страницу со всеми категориями товаров"""
    categories = Category.objects.order_by('name')
    context = {'categories': categories}
    return render(request, 'marketplaces/categories.html', context)

def category(request, category_id):
    """Выводит страницу со всеми товарами по категории"""
    category = Category.objects.get(id=category_id)
    products = category.product_set.order_by('-date_added')
    context = {'category': category, 'products': products}
    return render(request, 'marketplaces/category.html', context)

def products(request):
    """Выводит страницу со всеми товарами"""
    products = Product.objects.order_by('name')
    context = {'products': products}
    return render(request, 'marketplaces/products.html', context)

# def product(request, product_id):
#     """Выводит страницу со всеми товарами по категории"""
#     product = Product.objects.get(id=product_id)
#     #products = category.product_set.order_by('-date_added')
#     context = {'product': product}
#     return render(request, 'marketplaces/product.html', context)

def product(request, product_id):
    """Выводит страницу товара"""
    product = get_object_or_404(Product, id=product_id)
    cart_product_form = CartAddProductForm()
    context = {'product': product, 'cart_product_form': cart_product_form}
    return render(request, 'marketplaces/product.html', context)