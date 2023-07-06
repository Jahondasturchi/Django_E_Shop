from django.forms import ModelForm
from .models.products import Product
class ProructForm(ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'rasmi', 'narxi']


class ProructFormNew(ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'rasmi', 'narxi', 'category']