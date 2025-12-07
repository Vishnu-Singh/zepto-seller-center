from rest_framework import serializers
from .models import Product, ProductImage, ProductAttribute


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image_url', 'is_primary', 'display_order', 'created_at']


class ProductAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttribute
        fields = ['id', 'attribute_name', 'attribute_value']


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    attributes = ProductAttributeSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'sku', 'name', 'description', 'price', 'cost_price', 
                  'category', 'brand', 'status', 'weight', 'created_at', 
                  'updated_at', 'images', 'attributes']
        read_only_fields = ['created_at', 'updated_at']


class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['sku', 'name', 'description', 'price', 'cost_price', 
                  'category', 'brand', 'status', 'weight']
