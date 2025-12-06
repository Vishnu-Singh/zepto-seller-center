from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from lxml import etree
from .models import Report


@csrf_exempt
@require_http_methods(["GET", "POST"])
def reports_soap_service(request):
    """SOAP Service for Reports operations."""
    if request.method == 'GET':
        wsdl = '''<?xml version="1.0" encoding="UTF-8"?>
<definitions name="ReportsService"
             targetNamespace="http://zepto.com/reports/soap"
             xmlns="http://schemas.xmlsoap.org/wsdl/">
    <service name="ReportsService">
        <documentation>Reports Management SOAP Service</documentation>
    </service>
</definitions>'''
        return HttpResponse(wsdl, content_type='text/xml')
    
    try:
        response = '''<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <GetReportResponse>
            <result>Reports SOAP service is active. {} reports available.</result>
        </GetReportResponse>
    </soap:Body>
</soap:Envelope>'''.format(Report.objects.count())
        return HttpResponse(response, content_type='text/xml')
    except Exception as e:
        error_response = '''<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <soap:Fault>
            <faultstring>{}</faultstring>
        </soap:Fault>
    </soap:Body>
</soap:Envelope>'''.format(str(e))
        return HttpResponse(error_response, content_type='text/xml', status=500)
