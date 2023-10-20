from django import forms
from .models import Gun,Category


class GunForm(forms.Form):
    name        = forms.CharField(max_length=100)
    image       = forms.ImageField(required=False)
    price       = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea)
    in_stock    = forms.BooleanField(required=False)
    category    = forms.ModelChoiceField(queryset=Category.objects.all())