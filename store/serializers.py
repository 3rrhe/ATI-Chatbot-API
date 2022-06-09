from rest_framework import serializers
from store.models import Product, Client, Brand


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = \
            (
                'id',
                'name',
                'brand',
                'quantity',
                'price',
                'iva',
                'priceIva',
                'image',
            )


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = \
            (
                'id',
                'first_name',
                'last_name',
                'address',
                'phone',
            )


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = \
            (
                'id',
                'name',
                'description',
            )
