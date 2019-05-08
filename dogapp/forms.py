from django import forms
from .models import Dog, Customer

class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['name', 'color', 'race', 'gender']
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'age', 'email']