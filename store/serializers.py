from rest_framework import serializers
from store.models import Product


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = \
            (
                'id',
                'name',
                'brand',
                'price',
                'iva',
                'priceIva',
            )
