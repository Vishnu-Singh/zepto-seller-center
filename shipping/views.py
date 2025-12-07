from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Shipment
from .serializers import ShipmentSerializer


class ShipmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing shipments.
    """
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    
    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        """Update shipment status"""
        shipment = self.get_object()
        new_status = request.data.get('status')
        
        if new_status not in dict(Shipment.STATUS_CHOICES):
            return Response(
                {"error": "Invalid status"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        shipment.status = new_status
        shipment.save()
        serializer = self.get_serializer(shipment)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def track(self, request):
        """Track shipment by tracking number"""
        tracking_number = request.query_params.get('tracking_number')
        if tracking_number:
            try:
                shipment = Shipment.objects.get(tracking_number=tracking_number)
                serializer = self.get_serializer(shipment)
                return Response(serializer.data)
            except Shipment.DoesNotExist:
                return Response(
                    {"error": "Shipment not found"}, 
                    status=status.HTTP_404_NOT_FOUND
                )
        return Response(
            {"error": "tracking_number parameter is required"}, 
            status=status.HTTP_400_BAD_REQUEST
        )
