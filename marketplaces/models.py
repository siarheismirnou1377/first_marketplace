from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        """Возвращает строковое значение представления модели"""
        return self.name

class Product(models.Model):
    """Класс товара, который может заказать клиент"""
    category = models.ForeignKey(Category, on_delete = models.PROTECT)
    name = models.CharField(max_length=50)
    price = models.IntegerField("price")
    date_added = models.DateTimeField(auto_now_add=True)
    
       
    class Meta:
        verbose_name_plural = "Products"
    
    def __str__(self):
        """Возвращает строковое значение представления модели"""
        return self.name 
