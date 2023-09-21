
# from django.http import HttpResponse
# from django.template import loader

# def welcome (request):
#  template = loader.get_template("myfirst.html")
#  return HttpResponse(template.render())

# Create your views here.
import random
from . models import *
from django.http import HttpResponse
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response
from .response_serializers import *
from django.db.models import Q
from django.shortcuts import render
from . request_serializers import *
from django.core.files.base import ContentFile
import base64
from rest_framework import authentication,permissions
from authentication.utils import *


def get_water_management_details(request):
#   customers = Customer.objects.all().order_by('name')
#   supplier = Supplier.objects.all().order_by('-name')
#   watercan_prices = Watercan.objects.all().filter(price__gt = 30)
#   watercan = Watercan.objects.exclude(brand = 'waterman')
#   first_customer = Customer.objects.first()
#   last_customer = Customer.objects.last()
#   customers_list = Customer.objects.values_list('name',flat = True)
     #template = loader.get_template('customers.html')

  content = {
    'customers' : 'naresh',
    'supplier' : 2000,
    'watercan' : 'aqua'
   #  'watercan_prices' : watercan_prices,
   #  'first_customer' : first_customer,
   #  'last_customer' : last_customer,
   #  'customers_list' : customers_list
  }
  #return HttpResponse(template.render(content, request))
  return render(request,'myfirst.html',content)

class AddUserInfo(APIView):
   authentication_classes = [authentication.TokenAuthentication]
   permission_classes = [permissions.IsAuthenticated]
   def post(self,request):
      data = request.data   
      validation = AddUserInfoSerializer(data = data)
      if validation.is_valid():
         if 'id' not in data:
            if User.objects.filter(email = data['email']).count() == 0:
               user = User.objects.create(username = data['email'],password =data ['password'],email = data['email'])
               user.first_name = data['first_name']
               user.last_name = data['last_name']
               user.save()
               token = get_token_by_user(user)
               user_authentication = UserAuthentication.objects.create(user = user)
               if 'is_admin' in data:
                  user_authentication.is_admin = data['is_admin']
               if 'is_supplier' in data:
                  user_authentication.is_supplier = data['is_supplier']
               if 'is_customer' in data:
                  user_authentication.is_customer = data['is_customer']
               if 'is_employee' in data:
                  user_authentication.is_employee = data['is_employee']
               user_authentication.save()
               userInfoForm = {}
               #supplierForm['name'] = data['name']
               userInfoForm['contact_number'] = data['contact_number']
               #supplierForm['email'] = data ['email']
               userInfoForm['address'] = data ['address']

               UserInfo.objects.create(user = user ,**userInfoForm,user_authentication = user_authentication)

               return Response({"Message":"UserInfo added successfully"})
            else:
               return Response({"Message":"UserInfo already exists"})
         else:
            supplier = UserInfo.objects.get(user_id = data['id'])
            # user = User.objects.get(id = data['id'  ])
            if 'first_name' in data:
              supplier.user.first_name = data['first_name']
              supplier.user.save()
            if 'last_name' in data:
              supplier.user.last_name = data['last_name']
              supplier.user.save()
            if 'contact_number' in data:
             supplier.contact_number =data['contact_number']
            if 'address' in data :
             supplier.address = data['address']
             supplier.save()
            return Response({"Message":"supplier details has been updated successfully"})
      else:
         return Response({"Message":"invalid params"})

class GetUserInfos(APIView):
   authentication_classes = [authentication.TokenAuthentication]
   permission_classes = [permissions.IsAuthenticated]
   def post(self,request):
      data = request.data 
      # supplier_data = UserInfo.objects.all()#filter(name__istartswith = data['name'])
      # serializer_supplier = SupplierSerializers(supplier_data,many = True)
      # return Response(serializer_supplier.data)
      if 'is_supplier' in data:
         supplier_data = UserInfo.objects.filter(user_authentication__is_supplier = data['is_supplier'])
         supplier_serializer = UserInfoSerializer(supplier_data,many=True)
         return Response(supplier_serializer.data)

      if 'is_customer' in data :
         customer_data = UserInfo.objects.filter(user_authentication__is_customer = data['is_customer'])
         customer_serializer = UserInfoSerializer(customer_data,many = True)
         return Response(customer_serializer.data)

class GetUserDetails(APIView):
   authentication_classes = [authentication.TokenAuthentication]
   permission_classes = [permissions.IsAuthenticated]
   def post(self,request):
      data = request.data
      supplier_data = UserInfo.objects.get( id = data['id'])
      supplier_serializer = UserInfoSerializer(supplier_data)
      return Response(supplier_serializer.data)


class AddWatercan(APIView):
   authentication_classes =  [authentication.TokenAuthentication]
   permission_classes = [permissions.IsAuthenticated]
   def post(self,request):
      data = request.data

      validation = AddWatercanSerializer(data = data)
      if validation.is_valid():
         if 'id' not in data:
            if Watercan.objects.filter(brand = data['brand']).count() == 0:
               watercanForm = {}
               watercanForm['brand'] = data['brand']
               watercanForm['size'] = data['size']
               watercanForm['price'] = data['price']
               watercanForm['is_available'] = data['is_available']
               watercanForm['supplier_id'] = data['supplier_id']
               if 'photo' in data:
                  image_data = ContentFile(base64.b64decode(data['photo']))
                  file_name = str(random.randint(111111,999999))+'.jpeg'
               watercan = Watercan.objects.create(**watercanForm)
               watercan.photo.save(file_name,image_data,save = True)


               return Response ({"Message":"watercan added successfully"})
            else:
               return Response({"Message":"name is already exists"})
         else:
            watercan = Watercan.objects.get(id = data['id'])
            if 'brand'  in data:
               watercan.brand = data['brand']
            if 'size'  in data:
               watercan.size = data['size']
            if 'price'  in data:
               watercan.price = data['price']
            if 'is_available' in data:
               watercan.is_available = data['is_available']
            if 'supplier_id' in data:
               watercan.supplier_id = data['supplier_id']
            if 'photo' in data:
                  image_data = ContentFile(base64.b64decode(data['photo']))
                  file_name = str(random.randint(111111,999999))+'.jpg'
            watercan.save()
            watercan.photo.save(file_name,image_data,save = True)
            
            return Response({"Message":"watercan has been updated sucessfully"})
      else:
         return Response({'Message':'invalid params'})

class GetWatercans(APIView):
   def post (self,request):
      data = request.data
      watercan_data = Watercan.objects.all()#filter(photo = data['photo'])
      serializer_watercan = WatercanSerializers(watercan_data,many = True)
      return Response(serializer_watercan.data)
   
class GetWatercanDetails(APIView):
   def post(self,request):
      data = request.data
      watercan_data = Watercan.objects.get(id = data ['id'])
      serializer_watercan = WatercanSerializers(watercan_data)
      return Response(serializer_watercan.data)
      






      
# class GetCustomers(APIView):
#    authentication_classes = [authentication.TokenAuthentication]
#    permission_classes = [permissions.IsAuthenticated]
#    def post(self,request):
#       data = request.data
#       customer_data = UserInfo.objects.all()#filter(name = data['name'])
#       serializer_customer = CustomerSerializers(customer_data,many = True)
#       return Response(serializer_customer.data)
      
# class AddCustomer(APIView):
#   authentication_classes = [authentication.TokenAuthentication]
#   permission_classes = [permissions.IsAuthenticated]
#   def post(self,request):
#    data = request.data

#    validation = AddCustomerSerializer(data = data)
#    if validation.is_valid():
#       if 'id' not in data:
#          if User.objects.filter(email = data['email']).count() == 0:
#             user = User.objects.create(username = data['email'],password = data ['password'],email = data['email'])
#             user.first_name = data['first_name']
#             user.last_name = data['last_name']
#             user.save()
#             customerForm = {}
#             customerForm['contact_number'] = data['contact_number']
#             customerForm['email']= data['email']
#             customerForm['address'] = data['address']

#             UserInfo.objects.create(**customerForm)

#             return Response({"Message":"customer added successfully"})
#          else:
#             return Response({"Message":"name already exists"})
#       else:
#          customer = UserInfo.objects.get(id =data['id'])
#          if 'first_name' in data:
#             customer.user.first_name = data['name']
#          if 'last_name' in data:
#             customer.user.last_name = data['contact_number']
#          if 'email' in data:
#             customer.user.email = data['email']
#          if 'address' in data:
#             customer.address = data['address']
#          customer.save()
#          return Response({"Message":"customer detials updated successfully"})
#    else:
#       return Response({"Message":"invalid params"})   

# views.py

