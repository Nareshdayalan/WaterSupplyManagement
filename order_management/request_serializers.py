from rest_framework import serializers
from watercan_supply_management.models import Watercan

class WaterCanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watercan
        fields = '__all__'


class AddOrderSerializer(serializers.Serializer):
    date_ordered = serializers.DateTimeField(required = True)
    total_amount = serializers.IntegerField(required = True)
    is_completed = serializers.BooleanField(required = True)
    watercan_info = WaterCanSerializer(required = False)


class AddPaymentSerializer(serializers.Serializer):
    amount = serializers.IntegerField(required = True)
    date_paid = serializers.DateTimeField(required = True)
    customer_id = serializers.UUIDField(required = True)
    order_id =  serializers.UUIDField(required = True)