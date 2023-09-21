from django.urls import path
from . import views

urlpatterns = [
path('addOrder',views.AddOrder.as_view(),name = 'addOrder'),
path('getOrders',views.GetOrders.as_view(),name = 'getOrders'),
path('getOrderDetails',views.GetOrderDetails().as_view(),name = 'getOrderDetails'),
path('addPayments',views.AddPayment.as_view(),name = 'addPayments'),
path('getPayment',views.GetPayments.as_view(),name = 'getPayment'),
path('getPaymentDetails',views.GetPaymentDetails.as_view(),name = 'getPaymentDetails')


]