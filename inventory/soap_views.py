from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from lxml import etree
from .models import InventoryItem


@csrf_exempt
@require_http_methods(["GET", "POST"])
def inventory_soap_service(request):
    """SOAP Service for Inventory operations."""
    if request.method == 'GET':
        wsdl = '''<?xml version="1.0" encoding="UTF-8"?>
<definitions name="InventoryService"
             targetNamespace="http://zepto.com/inventory/soap"
             xmlns="http://schemas.xmlsoap.org/wsdl/">
    <service name="InventoryService">
        <documentation>Inventory Management SOAP Service</documentation>
    </service>
</definitions>'''
        return HttpResponse(wsdl, content_type='text/xml')
    
    try:
        response = '''<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <GetInventoryResponse>
            <result>Inventory SOAP service is active. {} items available.</result>
        </GetInventoryResponse>
    </soap:Body>
</soap:Envelope>'''.format(InventoryItem.objects.count())
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
