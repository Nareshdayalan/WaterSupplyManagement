from rest_framework import serializers
from .models import *



class UserInfoSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    class Meta:
        model = UserInfo
        fields = ['first_name','last_name','email','contact_number','address']
    def get_first_name(self,obj):
        return obj.user.first_name
    def get_last_name(self,obj):
        return obj.user.last_name
    def get_email(self,obj):
        return obj.user.email

# class CustomerSerializers(serializers.ModelSerializer):
#     first_name = serializers.SerializerMethodField()
#     last_name = serializers.SerializerMethodField()
#     email = serializers.SerializerMethodField()
#     class Meta:
#         model  = UserInfo
#         fields = ['first_name','last_name','name','address']
    
    # def get_first_name(self,obj):
    #     return obj.user.first_name
    

class WatercanSerializers(serializers.ModelSerializer):
    supplier_details = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()
    class Meta:
        model = Watercan
        fields = ['brand','supplier_details','photo']
    def get_supplier_details(self,obj):
        return {obj.supplier.user.first_name,obj.supplier.user.last_name,obj.supplier.address}
    def get_photo(self, obj):
        return obj.photo.url
