from django.urls import path
from . import views

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
]
 