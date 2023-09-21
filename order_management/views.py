from .models import *
from django.http import HttpResponse
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response
from .response_serializers import *
from watercan_supply_management.models import *
from .request_serializers import *


class AddOrder(APIView):
    def post(self,request):
        data = request.data
        validation = AddOrderSerializer(data = data)
        if validation.is_valid():
            if 'id' not in data:
                orderForm = {}                                                                                                                                                  
                orderForm['date_ordered'] = data['date_ordered']
                orderForm['total_amount'] = data['total_amount']
                orderForm['is_completed'] = data['is_completed']
                watercan_ids = data['watercan_info_id']
                order_form_create = Order.objects.create(**orderForm)
                order_form_create.watercan_info.add(*watercan_ids)
                
                return Response({"Message":"order added successFully"})
            else:
                order = Order.objects.get(id = data['id'])
                if 'date_ordered' in data:
                    order.date_ordered = data['date_ordered']
                if 'total_amount' in data:
                    order.total_amount = data['total_amount']
                if 'is_completed' in data:
                    order.is_completed = data['is_completed']
                if 'watercan_info' in data:
                    order.watercan_info.set(data['watercan_info'])
                order.save()
                return Response({"Message":"order detials updated successfully "})   
        else:
            return Response({"Message":"invalid params"})     

class GetOrders(APIView):
    def post(self,request):
        data = request.data
        order_data = Order.objects.all()
        serializers_order = OrderSerializers(order_data,many = True)
        return Response(serializers_order.data)

class GetOrderDetails(APIView):
    def post(self,request):
        data = request.data
        order_data = Order.objects.get(id = data['id'])
        serializers_order = OrderSerializers(order_data)
        return Response (serializers_order.data) 
       

    
class AddPayment(APIView):
    def post(self,request):
        data = request.data
        validation = AddPaymentSerializer(data = data)
        if validation.is_valid():
            if 'id' not in data:
                paymentForm = {}
                paymentForm['amount'] = data['amount']
                paymentForm['date_paid'] = data['date_paid']
                paymentForm['customer_id'] =data['customer_id']
                paymentForm['order_id'] = data['order_id']
                # customerForm= {}
                # # customerForm['name'] = data['customer']['name']  
                # # customerForm['contact_number'] = data['customer']['contact_number']            
                # # customerForm['email'] = data['customer']['email']            
                # # customerForm['address'] = data['customer']['address']  
                # customer =Customer.objects.create(**customerForm)          
                Payment.objects.create(**paymentForm)
                return Response({"Message":"payment added successFully"})
            else:
                payment = Payment.objects.get(id = data['id'])
                if 'amount' in data:
                    payment.amount = data['amount']
                if 'date_paid' in data:
                    payment.date_paid = data['date_paid']
                if 'customer_id' in data:
                    payment.customer = data['customer_id']
                if 'order_id' in data:
                    payment.order = data['order_id']
                payment.save()
                return Response({"Message":"payment has been updated successfully"})
        else:
            return Response({"Message":"invalid params"})
        
class GetPayments(APIView):
    def post(self,request):
        data = request.data
        payment_data = Payment.objects.all()
        serializer_payment = PaymentSerializers(payment_data,many = True)
        return Response(serializer_payment.data)

class GetPaymentDetails(APIView):
    def post(self,request):
        data = request.data
        payment_data = Payment.objects.get(id = data['id'])
        serializer_payment = PaymentSerializers(payment_data)
        return Response(serializer_payment.data)          


        

    
