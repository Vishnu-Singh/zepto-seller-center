from rest_framework import serializers
from .models import Transaction, Payout


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'transaction_id', 'transaction_type', 'order_number', 
                  'amount', 'currency', 'description', 'created_at']
        read_only_fields = ['created_at']


class PayoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payout
        fields = ['id', 'payout_id', 'amount', 'currency', 'status', 
                  'bank_account', 'notes', 'created_at', 'completed_at']
        read_only_fields = ['created_at', 'completed_at']
