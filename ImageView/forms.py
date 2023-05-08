from django import forms
from .models import Image, Category

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['Title', 'Description', 'Category', 'Images']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
