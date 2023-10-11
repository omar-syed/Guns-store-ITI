from django import forms
from .models import Gun

class GunForm(forms.ModelForm):
    class Meta:
        model = Gun
        fields = ['id','name', 'image','price','description','in_stock']  # Add other fields as needed
