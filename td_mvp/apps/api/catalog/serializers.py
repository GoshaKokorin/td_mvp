from rest_framework import serializers

from td_mvp.apps.catalog.models import Category, Product, ProductImage, ProductCharacteristic


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'image', 'is_active_on_main']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image', 'position']


class ProductCharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCharacteristic
        fields = ['name', 'value', 'position']


class ProductListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    product_images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['category', 'slug', 'name', 'short_description', 'product_images', 'price']


class ProductDetailSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True, read_only=True)
    category = serializers.StringRelatedField(read_only=True)
    product_characteristics = ProductCharacteristicSerializer(many=True, read_only=True)
    related_products = ProductListSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'category', 'slug', 'name', 'description', 'price', 'delivery', 'product_images',
            'product_characteristics', 'related_products',
        ]