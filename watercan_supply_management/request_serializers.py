from rest_framework import serializers

class AddUserInfoSerializer(serializers.Serializer):
    #name = serializers.CharField(required = True)
    contact_number = serializers.IntegerField(required = False)
    email = serializers.EmailField(required = False)
    address = serializers.CharField(required = False)
    last_name = serializers.CharField(required = False)
    


class AddWatercanSerializer(serializers.Serializer):
    brand =serializers.CharField(required = True)
    size =serializers.IntegerField(required =True)
    price = serializers.IntegerField(required = True)
    is_available = serializers.BooleanField(required=True)
    supplier_id = serializers.UUIDField(required = True)

# class AddCustomerSerializer(serializers.Serializer):
#     #name = serializers.CharField(required = True)
#     contact_number = serializers.IntegerField(required = True)
#     email = serializers.EmailField(required = True)
#     address = serializers.CharField(required = True)

