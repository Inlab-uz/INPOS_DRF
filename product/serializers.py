from rest_framework import serializers

from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'category', 'bar_code', 'name', 'price', 'stock', 'available', 'image', 'description', 'updated_at']


class CategorySerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Category
        fields = ['title', 'description', 'product']
