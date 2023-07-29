from django.shortcuts import get_object_or_404, render
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.shortcuts import render, redirect
from .forms import CategoryForm, ProductForm


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

def product(request, product_id):
    """Выводит страницу товара"""
    product = get_object_or_404(Product, id=product_id)
    cart_product_form = CartAddProductForm()
    context = {'product': product, 'cart_product_form': cart_product_form}
    return render(request, 'marketplaces/product.html', context)

def new_category(request):
    """Определяет новую категорию"""
    if request.method != 'POST':
        # Данные не отправились, создается пустая форма.
        form = CategoryForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('marketplaces:categories')
    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'marketplaces/new_category.html', context)

def new_product(request):
    """Добавляет новый товар"""
    # products = Category.objects.get(id=products_id)
    if request.method != 'POST':
        # Данные не отправились, создается пустая форма.
        form = ProductForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = ProductForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('marketplaces:products')
    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'marketplaces/new_product.html', context)