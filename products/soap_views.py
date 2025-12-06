from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from lxml import etree
from .models import Product


@csrf_exempt
@require_http_methods(["GET", "POST"])
def product_soap_service(request):
    """
    SOAP Service for Product operations.
    
    Simplified SOAP implementation that handles basic product operations.
    """
    if request.method == 'GET':
        # Return WSDL
        wsdl = '''<?xml version="1.0" encoding="UTF-8"?>
<definitions name="ProductService"
             targetNamespace="http://zepto.com/products/soap"
             xmlns:tns="http://zepto.com/products/soap"
             xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
             xmlns="http://schemas.xmlsoap.org/wsdl/">
    <message name="GetProductRequest">
        <part name="product_id" type="xsd:int"/>
    </message>
    <message name="GetProductResponse">
        <part name="result" type="xsd:string"/>
    </message>
    <portType name="ProductPortType">
        <operation name="GetProduct">
            <input message="tns:GetProductRequest"/>
            <output message="tns:GetProductResponse"/>
        </operation>
    </portType>
    <binding name="ProductBinding" type="tns:ProductPortType">
        <soap:binding style="rpc" transport="http://schemas.xmlsoap.org/soap/http"/>
        <operation name="GetProduct">
            <soap:operation soapAction="GetProduct"/>
            <input><soap:body use="literal"/></input>
            <output><soap:body use="literal"/></output>
        </operation>
    </binding>
    <service name="ProductService">
        <port name="ProductPort" binding="tns:ProductBinding">
            <soap:address location="http://localhost:8000/products/soap/"/>
        </port>
    </service>
</definitions>'''
        return HttpResponse(wsdl, content_type='text/xml')
    
    # Handle POST (SOAP requests)
    try:
        # Parse SOAP request
        root = etree.fromstring(request.body)
        
        # Simple response
        response = '''<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <GetProductResponse>
            <result>Product SOAP service is active. {} products available.</result>
        </GetProductResponse>
    </soap:Body>
</soap:Envelope>'''.format(Product.objects.count())
        
        return HttpResponse(response, content_type='text/xml')
    except Exception as e:
        error_response = '''<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <soap:Fault>
            <faultcode>soap:Server</faultcode>
            <faultstring>{}</faultstring>
        </soap:Fault>
    </soap:Body>
</soap:Envelope>'''.format(str(e))
        return HttpResponse(error_response, content_type='text/xml', status=500)
