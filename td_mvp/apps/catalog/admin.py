from django.contrib import admin

from .models import Category, Product, ProductImage, ProductCharacteristic


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class ProductImageInline(admin.TabularInline):
    fields = ['position', 'image']
    model = ProductImage
    extra = 0


class ProductCharacteristicInline(admin.TabularInline):
    fields = ['position', 'name', 'value']
    model = ProductCharacteristic
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'is_active']
    list_editable = ['is_active']
    search_fields = ['name']
    inlines = [ProductCharacteristicInline, ProductImageInline]
    fieldsets = [(
        None, {
            'fields': [
                'category', 'name', 'price', 'is_active',
            ]
        },
    ), (
        'Описание', {
            'classes': ['collapse'],
            'fields': ['short_description', 'description', 'delivery']
        },
    )]
