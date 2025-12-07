from django.contrib import admin
from .models import Product, ProductImage, ProductAttribute


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['sku', 'name', 'category', 'price', 'status', 'created_at']
    list_filter = ['status', 'category', 'created_at']
    search_fields = ['sku', 'name', 'description', 'category', 'brand']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [ProductImageInline, ProductAttributeInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('sku', 'name', 'description')
        }),
        ('Pricing', {
            'fields': ('price', 'cost_price')
        }),
        ('Categorization', {
            'fields': ('category', 'brand')
        }),
        ('Status & Weight', {
            'fields': ('status', 'weight')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image_url', 'is_primary', 'display_order']
    list_filter = ['is_primary']
    search_fields = ['product__sku', 'product__name']


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ['product', 'attribute_name', 'attribute_value']
    search_fields = ['product__sku', 'attribute_name', 'attribute_value']
