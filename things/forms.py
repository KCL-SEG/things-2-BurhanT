"""Forms of the project."""
from django import forms
from .models import Thing
from django.core.validators import MinValueValidator, MaxValueValidator

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        name = forms.CharField(label="name", max_length = 35)
        description = forms.CharField(label="description",max_length=120,required=False)
        quantity = forms.IntegerField(label="quantity",validators=[MinValueValidator(0),MaxValueValidator(50)])
        widgets = { 'description': forms.Textarea(), 'quantity': forms.NumberInput() }
