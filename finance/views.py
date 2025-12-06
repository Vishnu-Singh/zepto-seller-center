from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Transaction, Payout
from .serializers import TransactionSerializer, PayoutSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    """API endpoint for managing transactions."""
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
    @action(detail=False, methods=['get'])
    def by_type(self, request):
        """Get transactions by type"""
        transaction_type = request.query_params.get('type')
        if transaction_type:
            transactions = self.queryset.filter(transaction_type=transaction_type)
            serializer = self.get_serializer(transactions, many=True)
            return Response(serializer.data)
        return Response({"error": "type parameter is required"}, status=400)


class PayoutViewSet(viewsets.ModelViewSet):
    """API endpoint for managing payouts."""
    queryset = Payout.objects.all()
    serializer_class = PayoutSerializer
    
    @action(detail=False, methods=['get'])
    def pending(self, request):
        """Get pending payouts"""
        payouts = self.queryset.filter(status='pending')
        serializer = self.get_serializer(payouts, many=True)
        return Response(serializer.data)
