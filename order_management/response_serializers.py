from rest_framework import serializers
from .models import *
from watercan_supply_management.models import *

    
class OrderSerializers(serializers.ModelSerializer):
    watercan_details = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ['date_ordered','total_amount','is_completed','watercan_details']
    
    def get_watercan_details(self,obj):
        watercan = []
        for i in obj.watercan_info.all():
            watercan.append({"brand":i.brand,"price":i.price})
        return watercan
    
class PaymentSerializers(serializers.ModelSerializer):
    customer_details = serializers.SerializerMethodField()
    order_details = serializers.SerializerMethodField()
    class Meta:
        model = Payment
        fields = ['amount','date_paid','customer_details','order_details']
    def get_customer_details(self,obj):
        return {"name":obj.customer.user.first_name,"contact_number":obj.customer.contact_number,"address":obj.customer.address}
    def get_order_details(self,obj):
        return {"total_amount":obj.order.total_amount}
  