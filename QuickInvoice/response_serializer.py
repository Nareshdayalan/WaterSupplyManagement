from .models import Invoice, InvoiceDetail
from rest_framework import serializers


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'date', 'customer_name']

class InvoiceDetailSerializer(serializers.ModelSerializer):
    invoice = serializers.SerializerMethodField()
    class Meta:
        model = InvoiceDetail
        fields = ['invoice','id', 'invoice', 'description', 'quantity', 'unit_price', 'price']
    def get_invoice(self,obj):
        return {"customer_name":obj.invoice.customer_name,"date":obj.invoice.date}

