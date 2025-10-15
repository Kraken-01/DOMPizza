from django import forms
from .models import Order

class CheckoutForm(forms.ModelForm):
    ORDER_TYPE_CHOICES = [
        ('PICKUP', 'Pickup'),
        ('DELIVERY', 'Delivery'),
    ]
    
    customer_name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'placeholder': 'Full Name',
            'class': 'form-input'
        })
    )
    
    customer_email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email Address',
            'class': 'form-input'
        })
    )
    
    customer_phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'placeholder': 'Phone Number (e.g., 555-123-4567)',
            'class': 'form-input'
        })
    )
    
    order_type = forms.ChoiceField(
        choices=ORDER_TYPE_CHOICES,
        widget=forms.RadioSelect(attrs={
            'class': 'radio-input'
        }),
        initial='PICKUP'
    )
    
    delivery_address = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'placeholder': 'Street Address\nCity, State ZIP',
            'class': 'form-textarea',
            'rows': 3
        })
    )
    
    special_instructions = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'placeholder': 'Any special instructions? (optional)',
            'class': 'form-textarea',
            'rows': 3
        })
    )
    
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_email', 'customer_phone', 'order_type']
    
    def clean(self):
        cleaned_data = super().clean()
        order_type = cleaned_data.get('order_type')
        delivery_address = cleaned_data.get('delivery_address')
        
        if order_type == 'DELIVERY' and not delivery_address:
            raise forms.ValidationError('Delivery address is required for delivery orders.')
        
        return cleaned_data

