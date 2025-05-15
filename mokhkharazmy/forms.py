from django import forms  
from .models import Product, Customer 

class ProductForm(forms.ModelForm):  
    class Meta:  
        model = Product  
        fields = ['name', 'en_name', 'picture']

class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(
        label="نام",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'لطفاً نام خود را وارد کنید'
        })
    )
    
    last_name = forms.CharField(
        label="نام خانوادگی",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'لطفاً نام خانوادگی خود را وارد کنید'
        })
    )

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name']