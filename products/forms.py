from django import forms
from .models import ProductAttribute, SubAttribute

class ProductAttributeForm(forms.ModelForm):
    subattribute = forms.ModelChoiceField(queryset=SubAttribute.objects.none(), required=False)
    value = forms.CharField(required=False)

    class Meta:
        model = ProductAttribute
        fields = ('attribute', 'subattribute', 'value')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['subattribute'].queryset = SubAttribute.objects.filter(attribute=self.instance.attribute)
        self.fields['attribute'].widget.attrs.update({'class': 'attribute-select'})
        self.fields['subattribute'].widget.attrs.update({'class': 'subattribute-select'})



    # def __init__(self, *args, **kwargs):
    #     category = kwargs.pop('category', None)
    #     super().__init__(*args, **kwargs)
    #     if category:
    #         self.fields['attribute'].queryset = Attribute.objects.filter(category=category)

from django import forms
from .models import Category

class ImportAttributesForm(forms.Form):
    csv_file = forms.FileField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
