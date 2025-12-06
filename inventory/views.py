from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import InventoryItem, StockMovement
from .serializers import InventoryItemSerializer, InventoryItemCreateUpdateSerializer, StockMovementSerializer


class InventoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing inventory.
    
    Endpoints:
    - GET /api/inventory/ - List all inventory items
    - POST /api/inventory/ - Create a new inventory item
    - GET /api/inventory/{id}/ - Retrieve an inventory item
    - PUT /api/inventory/{id}/ - Update an inventory item
    - DELETE /api/inventory/{id}/ - Delete an inventory item
    - GET /api/inventory/{id}/movements/ - Get stock movements
    - POST /api/inventory/{id}/adjust_stock/ - Adjust stock quantity
    - GET /api/inventory/low_stock/ - Get items with low stock
    """
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return InventoryItemCreateUpdateSerializer
        return InventoryItemSerializer
    
    @action(detail=True, methods=['get'])
    def movements(self, request, pk=None):
        """Get all stock movements for an inventory item"""
        item = self.get_object()
        movements = item.movements.all()
        serializer = StockMovementSerializer(movements, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def adjust_stock(self, request, pk=None):
        """Adjust stock quantity"""
        item = self.get_object()
        movement_type = request.data.get('movement_type', 'adjustment')
        quantity = int(request.data.get('quantity', 0))
        notes = request.data.get('notes', '')
        
        # Create stock movement record
        StockMovement.objects.create(
            inventory_item=item,
            movement_type=movement_type,
            quantity=quantity,
            notes=notes
        )
        
        # Update inventory
        if movement_type in ['in', 'return']:
            item.quantity_available += quantity
        elif movement_type == 'out':
            item.quantity_available -= quantity
        elif movement_type == 'adjustment':
            item.quantity_available = quantity
            
        item.save()
        
        serializer = self.get_serializer(item)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def low_stock(self, request):
        """Get items with low stock (needs reorder)"""
        items = [item for item in self.queryset.all() if item.needs_reorder]
        serializer = self.get_serializer(items, many=True)
        return Response(serializer.data)
