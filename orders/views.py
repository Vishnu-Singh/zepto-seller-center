from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderCreateUpdateSerializer, OrderItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing orders.
    
    Endpoints:
    - GET /api/orders/ - List all orders
    - POST /api/orders/ - Create a new order
    - GET /api/orders/{id}/ - Retrieve an order
    - PUT /api/orders/{id}/ - Update an order
    - PATCH /api/orders/{id}/ - Partial update an order
    - DELETE /api/orders/{id}/ - Delete an order
    - GET /api/orders/{id}/items/ - Get order items
    - POST /api/orders/{id}/update_status/ - Update order status
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return OrderCreateUpdateSerializer
        return OrderSerializer
    
    @action(detail=True, methods=['get'])
    def items(self, request, pk=None):
        """Get all items for an order"""
        order = self.get_object()
        items = order.items.all()
        serializer = OrderItemSerializer(items, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        """Update order status"""
        order = self.get_object()
        new_status = request.data.get('status')
        
        if new_status not in dict(Order.STATUS_CHOICES):
            return Response(
                {"error": "Invalid status"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        order.status = new_status
        order.save()
        serializer = self.get_serializer(order)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def by_status(self, request):
        """Get orders by status"""
        order_status = request.query_params.get('status', None)
        if order_status:
            orders = self.queryset.filter(status=order_status)
            serializer = self.get_serializer(orders, many=True)
            return Response(serializer.data)
        return Response({"error": "Status parameter is required"}, 
                       status=status.HTTP_400_BAD_REQUEST)
