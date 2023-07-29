from .models import Category, Product
from django import forms

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ['name']
        labels = {'name': ''}
        