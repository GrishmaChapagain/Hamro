from products.models import Product
from django import forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "category", "Image", "Price",
                  "Selling_Price", "Description", "Manufacturer"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the product title here..."
            }),
           
            "category": forms.Select(attrs={
                "class": "form-control"
            }),
            "Image": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),
            "Price": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Markedselling  price of the product..."
            }),
            "Selling_Price": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "dis price of the product..."
            }),
            "Description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Description of the product...",
                "rows": 5
            })

        }