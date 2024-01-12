from django.urls import path
from . import views

urlpatterns = [
    
    # path('logOutSSO',views.SignOutSSO.as_view(),name = 'signOutSSO')
    path("invoice",views.InvoicesCrud.as_view(),name = "getInvoice")
 ]
