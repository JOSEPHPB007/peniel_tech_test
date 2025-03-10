from django import forms
from .models import Members, Product

class MemberForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = ['name', 'discount']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['productname', 'price']
