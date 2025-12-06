from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product, ProductImage, ProductAttribute
from .serializers import (
    ProductSerializer, ProductCreateUpdateSerializer,
    ProductImageSerializer, ProductAttributeSerializer
)


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing products.
    
    Endpoints:
    - GET /api/products/ - List all products
    - POST /api/products/ - Create a new product
    - GET /api/products/{id}/ - Retrieve a product
    - PUT /api/products/{id}/ - Update a product
    - PATCH /api/products/{id}/ - Partial update a product
    - DELETE /api/products/{id}/ - Delete a product
    - GET /api/products/{id}/images/ - Get product images
    - GET /api/products/{id}/attributes/ - Get product attributes
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ProductCreateUpdateSerializer
        return ProductSerializer
    
    @action(detail=True, methods=['get'])
    def images(self, request, pk=None):
        """Get all images for a product"""
        product = self.get_object()
        images = product.images.all()
        serializer = ProductImageSerializer(images, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def attributes(self, request, pk=None):
        """Get all attributes for a product"""
        product = self.get_object()
        attributes = product.attributes.all()
        serializer = ProductAttributeSerializer(attributes, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def by_category(self, request):
        """Get products by category"""
        category = request.query_params.get('category', None)
        if category:
            products = self.queryset.filter(category=category)
            serializer = self.get_serializer(products, many=True)
            return Response(serializer.data)
        return Response({"error": "Category parameter is required"}, 
                       status=status.HTTP_400_BAD_REQUEST)
