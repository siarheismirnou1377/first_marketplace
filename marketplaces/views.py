from django.shortcuts import render
from .models import Category, Product

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

# def products(request):
#     """Выводит страницу со всеми продуктами"""
#     products = Product.objects.order_by('name')
#     context = {'products': products}
#     return render(request, 'marketplaces/products.html', context)