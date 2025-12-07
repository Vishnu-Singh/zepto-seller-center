from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Report
from .serializers import ReportSerializer


class ReportViewSet(viewsets.ModelViewSet):
    """API endpoint for managing reports."""
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    
    @action(detail=False, methods=['get'])
    def by_type(self, request):
        """Get reports by type"""
        report_type = request.query_params.get('type')
        if report_type:
            reports = self.queryset.filter(report_type=report_type)
            serializer = self.get_serializer(reports, many=True)
            return Response(serializer.data)
        return Response({"error": "type parameter is required"}, status=400)
    
    @action(detail=False, methods=['get'])
    def completed(self, request):
        """Get completed reports"""
        reports = self.queryset.filter(status='completed')
        serializer = self.get_serializer(reports, many=True)
        return Response(serializer.data)
