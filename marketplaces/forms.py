from .models import Category, Product
from django import forms

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ['name']
        labels = {'name': 'Name category'}
        
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'price']
        labels = {'category': 'Name category', 'name': 'Name product', 'price': 'Price'}