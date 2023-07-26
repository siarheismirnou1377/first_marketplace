from django.urls import path
from . import views
from cart import views as views_cart

app_name = "marketplaces"
urlpatterns = [
    # Главная страница
    path("", views.index, name="index"),
    # Страница категорий
    path("categories/", views.categories, name="categories"),
    # Страница всех товаров по категрии
    path('categories/<int:category_id>/', views.category, name='category'),
    # Страница всех товаров
    path('products/', views.products, name='products'),
    # Страница товара
    path('<int:product_id>/', views.product, name='product'),
    # Страница корзины
    path('cart/', views_cart.cart_detail, name='cart_detail'),
]
 