from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Invoice, InvoiceDetail
from .response_serializer import *

class InvoicesCrud(APIView):

    def get(self, request):
        data = request.data
        invoices = InvoiceDetail.objects.all()
        serializer = InvoiceDetailSerializer(invoices, many=True)
        return Response(serializer.data)
    
    def delete(self,request): 
        data = request.data
        invoice = Invoice.objects.filter(id = data["invoice_id"])
        invoice.delete()
        return Response({"Invoice deleted successfully"})
    
    def post(self,request):
        data = request.data
        if Invoice.objects.filter(customer_name = data["customer_name"]).count() == 0:
            invoiceDetailForm = {}
            invoiceDetailForm["description"] = data["description"]
            invoiceDetailForm["quantity"] = data["quantity"]
            invoiceDetailForm["unit_price"] = data["unit_price"]
            invoiceDetailForm["price"] = data["price"]
        
            invoiceForm = {}
            invoiceForm["date"] = data["date"]
            invoiceForm["customer_name"] = data["customer_name"]
            invoice = Invoice.objects.create(**invoiceForm)
            invoiceDetailForm["invoice"] = invoice
            InvoiceDetail.objects.create(**invoiceDetailForm)
            return Response("Invoice created successfully")
        else:
            return Response("Invoice already exists")
        

    def put(self, request):
        data = request.data
    
        invoice_detail = InvoiceDetail.objects.get(id=data["id"])
        if "date" in data:
            invoice_detail.invoice.date = data["data"]
        if "customer_name" in data:
             invoice_detail.invoice.customer_name = data["customer_name"]
        if "description" in data:
            invoice_detail.description = data["description"]
        if "quantity" in data:
            invoice_detail.quantity = data["quantity"]
        if "unit_price" in data:
            invoice_detail.unit_price = data["unit_price"]
        if "price" in data:
            invoice_detail.price = data["price"]
        invoice_detail.save()
        return Response({"Invoice updated successfully"})
                    