from django.contrib import admin
from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['report_id', 'report_type', 'status', 'start_date', 'end_date', 'created_at']
    list_filter = ['report_type', 'status', 'created_at']
    search_fields = ['report_id']
    readonly_fields = ['created_at', 'completed_at']
    
    fieldsets = (
        ('Report Information', {
            'fields': ('report_id', 'report_type', 'status')
        }),
        ('Date Range', {
            'fields': ('start_date', 'end_date')
        }),
        ('File', {
            'fields': ('file_url',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'completed_at'),
            'classes': ('collapse',)
        }),
    )
