from django.contrib import admin
from .models import Transaction, Payout


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['transaction_id', 'transaction_type', 'amount', 'currency', 'created_at']
    list_filter = ['transaction_type', 'currency', 'created_at']
    search_fields = ['transaction_id', 'order_number']
    readonly_fields = ['created_at']


@admin.register(Payout)
class PayoutAdmin(admin.ModelAdmin):
    list_display = ['payout_id', 'amount', 'currency', 'status', 'created_at']
    list_filter = ['status', 'currency', 'created_at']
    search_fields = ['payout_id', 'bank_account']
    readonly_fields = ['created_at', 'completed_at']
