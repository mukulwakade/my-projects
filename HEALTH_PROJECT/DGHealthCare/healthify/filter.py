import django_filters
from .models import ProductModel

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = ProductModel
        fields = ['name']