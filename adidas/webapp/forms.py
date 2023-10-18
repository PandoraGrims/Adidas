from django import forms
from multiupload.fields import MultiFileField

from .models import Product, ProductImage, Category, Size


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти")


class ProductForm(forms.ModelForm):
    image = MultiFileField(
        min_num=1,
        max_num=10,
        required=False
    )
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Выберите категорию")

    class Meta:
        model = Product
        fields = ['name', 'code', 'price', 'description', 'details', 'category', 'sizes']

        sizes = forms.ModelMultipleChoiceField(
            queryset=Size.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            required=False,
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['multiple'] = True




class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['product', 'image']
